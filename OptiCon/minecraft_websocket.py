from .server import Server
from .event import Event
from .command import Command
from .packet import Packet
from .agent import Agent
from .utils import Utils
import json, uuid
from typing import Callable, Awaitable, Optional

class MinecraftWebSocket(Server, Event, Command, Agent):
    command_responses = list()

    async def on_data(self, data: str):
        data = json.loads(data)
        header = data['header']
        body = data['body']
        messagePurpose = header['messagePurpose']
        if messagePurpose == Packet.Purpose.Event:
            eventName = body['eventName']
            properties = body['properties']
            await self.on_event(eventName, properties)
        elif messagePurpose == Packet.Purpose.CommandResponse:
            request_id = header['requestId']
            await self.on_command_response(request_id, body)

    def reset(self):
        super().reset()
        self.events = list()
        self.command_responses = list()

    async def add_event(self, event: str):
        if not self.has_event(event):
            super().add_event(event)
            packet = Packet(str(uuid.uuid4()), Packet.Purpose.Subscribe, eventName=event)
            await self.send_data(packet.encode())

    async def remove_event(self, event: str):
        if self.has_event(event):
            super().remove_event(event)
            packet = Packet(str(uuid.uuid4()), Packet.Purpose.Unsubscribe, eventName=event)
            await self.send_data(packet.encode())

    async def on_command_response(self, request_id: str, body: dict):
        for command_response in self.command_responses:
            if request_id == command_response[0]:
                await command_response[1](body)
                self.command_responses.remove(command_response)

    async def execute_command(self, command_line: str, call_back: Optional[Callable[[], Awaitable[None]]]):
        request_id = str(uuid.uuid4())
        packet = Packet(request_id, Packet.Purpose.CommandRequest, commandLine=command_line)
        await self.send_data(packet.encode())
        if call_back != None:
            self.command_responses.append([request_id, call_back])

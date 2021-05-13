import websockets, asyncio

class Server:
    def __init__(self, host: str = 'localhost', port: int = 8080):
        self.host = host
        self.port = port

    def run(self):
        self.server = websockets.serve(self.__connect, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

    async def __connect(self, conn, _):
        self.conn = conn
        await self.on_connect()
        await self.__recv()

    async def on_connect(self):
        pass

    async def on_disconnect(self):
        pass

    async def on_data(self, data: str):
        pass

    async def __recv(self):
        while True:
            try:
                data = await self.conn.recv()
                await self.on_data(data)
            except websockets.ConnectionClosed:
                await self.on_disconnect()
                self.reset()
                break

    def reset(self):
        self.conn = None

    async def send_data(self, data: str):
        await self.conn.send(data)

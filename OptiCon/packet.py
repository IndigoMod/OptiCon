import json

class Packet:
    class Purpose:
        Subscribe = 'subscribe'
        Unsubscribe = 'unsubscribe'
        Event = 'event'
        Error = 'error'
        CommandRequest = 'commandRequest'
        CommandResponse = 'commandResponse'

    VERSION = 1
    body = dict()

    def __init__(self, request_id: str, purpose: str, **kwargs):
        self.request_id = request_id
        self.purpose = purpose
        for key, value in kwargs.items():
            self.body[key] = value

    def encode(self) -> str:
        packet = {
            'header': {
                'requestId': self.request_id,
                'messagePurpose': self.purpose,
                'version': self.VERSION
            },
            'body': self.body
        }
        return json.dumps(packet)

from .packet import Packet
import json

class Utils:
    def decode_packet(pck):
        return json.JSONDecoder.decode(Packet.encode(pck))

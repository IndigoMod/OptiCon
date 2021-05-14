from .packet import Packet
import json


class Utils:
    def get_json_value(content, name):
        return content[name]

    def decode_json(itm):
        return json.JSONDecoder.decode(itm)

    def encode_json(itm):
        return json.JSONEncoder.encode(itm)

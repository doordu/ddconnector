import base64
import json

from ddconnector.exceptions import DecodeException

def decode(s: bytes):
    try:
        s = base64.decodebytes(s)
        s = json.loads(s)
        return s
    except Exception:
        raise DecodeException()
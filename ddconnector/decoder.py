import base64
import ujson as json

from ddconnector.exceptions import DecodeException

def decode(s: bytes):
    try:
        s = base64.decodebytes(s)
        s = json.loads(s)
        return s
    except Exception:
        raise DecodeException()
    
    
def encode(d: dict):
    try:
        s = json.dumps(d)
        s = base64.encodebytes(s.encode("utf-8"))
        return s + b'*'
    except Exception:
        raise DecodeException()
        
import json
import ujson


d = {'fd': 0, 'cmd': 'open_door', 'from_id': 0, 'guid': 'DD302WI201512A-1355', 'isClient': True, 'time': '2017-05-09 15:36:08', 'data': '{"room_id": 0}'}

def test_json():
    s = json.dumps(d)
    a = json.loads(s)

def test_ujson():
    #d = {'fd': 0, 'cmd': 'open_door', 'from_id': 0, 'guid': 'DD302WI201512A-1355', 'isClient': True, 'time': '2017-05-09 15:36:08', 'data': '{"room_id": 0}'}
    s = ujson.dumps(d)
    a = ujson.loads(s)


if __name__ == "__main__":
    import timeit
    print("json:", timeit.timeit("test_json()", setup="from __main__ import test_json"))
    print("ujson", timeit.timeit("test_ujson()", setup="from __main__ import test_ujson"))
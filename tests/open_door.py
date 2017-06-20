import asyncio
import uuid
import json
import base64
import time


@asyncio.coroutine
def open_door(loop):
    d = {'fd': 0, 'cmd': 'open_door', 'from_id': 0, 'guid': 'DD302WI201512A-1355', 'isClient': True, 'time': '2017-05-09 15:36:08', 'data': '{"room_id": 0}'}
    message = json.dumps(d)
    message = base64.encodebytes(message.encode('utf_8')) + b'*'
    reader, writer = yield from asyncio.open_connection('localhost', 9501,
                                                        loop=loop)
    writer.write(message)
    data = yield from reader.read(1024)
    writer.close()

start = time.time()

loop = asyncio.get_event_loop()
tasks = [open_door(loop) for i in range(1)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print("taken time: ", time.time() - start)

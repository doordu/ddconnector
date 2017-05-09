import asyncio
import uuid
import json
import base64
import time


@asyncio.coroutine
def open_door(loop):
    d = {'cmd': 'open_door', 'request_id': 'BDD4001610-1612', 'response_params': {'data': [{'door_guid': 'BDD4001610-1612', 'room_id': '4121694', 'floor': 1, 'operate_type': 2, 'device_type': '3', 'device_guid': '06877BEC-12E3-47CD-8D35-A936F71BA16E-a47a7898481eabf77a1a5ce061f7908b-193535', 'content': '%27%7b%22doorGuid%22%3a+%22BDD4001610-1612%22%2c+%22roomId%22%3a+%224121694%22%2c+%22userId%22%3a+%22193535%22%7d%27'}], 'message': '', 'success': True, 'totalCount': '0'}, 'response_type': False, 'token_id': ''}
    message = json.dumps(d)
    message = base64.encodebytes(message.encode('utf_8')) + b'*'
    reader, writer = yield from asyncio.open_connection('localhost', 9501,
                                                        loop=loop)
    writer.write(message)
    data = yield from reader.read(1024)
    print(data)
    writer.close()

start = time.time()

loop = asyncio.get_event_loop()
tasks = [open_door(loop) for i in range(1)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print("taken time: ", time.time() - start)

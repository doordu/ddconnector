import asyncio
import uuid
import json
import base64
import time


@asyncio.coroutine
def heart_beat(loop):
    d = {"guid":str(uuid.uuid4()),"cmd":"heart_beat","version":"5.8.000.0"}
    message = json.dumps(d)
    message = base64.encodebytes(message.encode('utf_8')) + b'*'
    reader, writer = yield from asyncio.open_connection('127.0.0.1', 9501,
                                                        loop=loop)
    writer.write(message)
    data = yield from reader.read(1024)
    #print(data)
    #writer.close()
       
start = time.time()

loop = asyncio.get_event_loop()
tasks = [heart_beat(loop) for i in range(10000)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print("taken: ", time.time() - start)

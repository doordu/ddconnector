import asyncio
import uuid
import json
import base64
import time


@asyncio.coroutine
def heart_beat(loop):
    #d = {"guid":str(uuid.uuid4()),"cmd":"heart_beat","version":"5.8.000.0"}
    d = {"guid":"testzz20170609","cmd":"heart_beat","version":"5.8.000.0"}
    message = json.dumps(d)
    message = base64.encodebytes(message.encode('utf_8')) + b'*'
    # swheart.doordu.com
    reader, writer = yield from asyncio.open_connection('localhost', 9501,
                                                        loop=loop)
    writer.write(message)
    data = yield from reader.read(1024)
    print(message)
    #writer.close()

start = time.time()

loop = asyncio.get_event_loop()
tasks = [heart_beat(loop) for i in range(1)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


print("taken time: ", time.time() - start)

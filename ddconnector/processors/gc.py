
import asyncio
import time
import gc

EXPIRED_SECONDS = 60 * 1  

@asyncio.coroutine
def gc(protocol, msg):
    """
    garbage collection
    """
    now = time.time()
    
    for p in list(protocol.server.doors.values()):
        if p.last_time != 0 and now - p.last_time > EXPIRED_SECONDS:
            p.transport.close()
        try:
            del protocol.server.doors[p.guid]
        except KeyError:
            pass

    response = "垃圾回收结束！"    
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    gc.collect()
    
    
import logging
import json
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
    before_gc_total = len(protocol.server.doors)
    
    for p in protocol.server.doors.values():
        if self.last_time != 0 and now - p.last_time > EXPIRED_SECONDS:
            p.transport.close()
            
    after_gc_total = len(protocol.server.doors)
    
    
    response = "垃圾回收结束！{0:d} -> {1:d}".format(before_gc_total, after_gc_total)    
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    gc.collect()
    
    
import logging
import json
import asyncio
import time

EXPIRED_DURATION = 300

@asyncio.coroutine
def gc(protocol, msg):
    """
    garbage collection
    """
    now = time.time()
    before_gc_total = len(protocol.server.protocols)
    
    for p in protocol.server.protocols:
        if now - p.last_time > EXPIRED_DURATION:
            try:
                p.transport.close() 
            except Exception:
                pass
            
            try:
                del protocol.server.protocols['guid']
            except KeyError:
                pass
            
    after_gc_total = len(protocol.server.protocols)
    
    
    response = "垃圾回收结束！{0:d} -> {1:d}".format(before_gc_total, after_gc_total)    
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    
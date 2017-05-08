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
    for p, t in protocol.server.transports:
        if now - t > EXPIRED_DURATION:
            try:
                p.close() 
            except Exception:
                pass
    
    response = "垃圾回收结束！"    
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    
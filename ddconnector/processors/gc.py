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
    before_gc_total = len(protocol.server.transports)
    
    for guid, (transport, last_ping) in protocol.server.transports.items():
        if now - last_ping > EXPIRED_DURATION:
            try:
                transport.close() 
            except Exception:
                pass
            
            try:
                del protocol.server.transports['guid']
            except KeyError:
                pass
            
    after_gc_total = len(protocol.server.transports)
    
    
    response = "垃圾回收结束！{0:d} -> {1:d}".format(before_gc_total, after_gc_total)    
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    
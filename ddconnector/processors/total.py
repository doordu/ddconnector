import logging
import json
import asyncio

from ddconnector.decoder import encode


@asyncio.coroutine
def total(protocol, msg):
    """
    获取连接总数
    """
    response = "{0:d}".format(len(protocol.server.transports))
        
    protocol.transport.write(response.encode("utf-8"))
    protocol.transport.close()
    
    
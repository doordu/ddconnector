import logging
import json
import asyncio

from ddconnector.decoder import encode


@asyncio.coroutine
def debug(protocol, msg):
    """
    动态配置
    """
    response = None
    if msg['enabled']:
        logging.getLogger().setLevel(logging.DEBUG)
        response = b"Debug level is enabled successfully!\n"
    else:
        logging.getLogger().setLevel(logging.ERROR)
        response = b"Debug level is disabled successfully!\n"
        
    protocol.transport.write(response)
    protocol.transport.close()
    
    
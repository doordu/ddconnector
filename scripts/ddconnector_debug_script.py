import logging
from logging.config import fileConfig
import configparser
import asyncio
import sys


import uvloop

from ddconnector.server import Server
from raven import Client
from raven_aiohttp import AioHttpTransport


@asyncio.coroutine
def debug(loop, ip='localhost', port=9501, enabled=False):
    reader, writer = yield from asyncio.open_connection(ip, port,
                                                        loop=loop)
    message = None
    if enabled:
        message = b'eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IHRydWV9*'
    else:
        message = b'eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IGZhbHNlfQ==*'

    writer.write(message)

    data = yield from reader.read(100)
    print('Received: %r' % data.decode())

    writer.close()
    

def main():
    config_file = '/etc/ddconnector.ini'
    
    if len(sys.argv) > 2:
        config_file = sys.argv[2]
    
    fileConfig(config_file)
    
    client = Client('https://ca252a631c4b437cac81ea0ad3e545ff:d31c83bc53b644138831c7c7d41ba661@sdlog.doordu.com:8205/17', transport=AioHttpTransport)
    config = configparser.ConfigParser()
    config.read(config_file)
    
    try:
        enabled = bool(int(sys.argv[1]))
        
        loop = uvloop.new_event_loop()
        loop.run_until_complete(debug(loop, 
                                      config['general']['server_ip'], 
                                      config['general']['listen_port'], 
                                      enabled))
        loop.close()
    except ValueError:
        print("ddconnector_debug_script enabled [0 or 1]")
    
    
    
if __name__ == "__main__":
    main()
    
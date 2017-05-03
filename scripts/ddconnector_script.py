import sys
import logging
from logging.config import fileConfig
import configparser

from ddconnector.server import Server
from raven import Client
from raven_aiohttp import AioHttpTransport

def main():
    config_file = '/etc/ddconnector.ini'
    
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    
    fileConfig(config_file)
    
    client = Client('https://ca252a631c4b437cac81ea0ad3e545ff:d31c83bc53b644138831c7c7d41ba661@sdlog.doordu.com:8205/17', transport=AioHttpTransport)
    config = configparser.ConfigParser()
    config.read(config_file)
    server = Server(config, client)
    server.run()
    
if __name__ == "__main__":
    main()
    
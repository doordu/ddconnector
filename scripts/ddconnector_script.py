import logging
import configparser

from ddconnector.server import Server
from raven import Client
from raven_aiohttp import AioHttpTransport

def main():
    logging.basicConfig(filename="ddconnector.log", 
                        level=logging.INFO,
                        format='%(asctime)s %(name)-4s %(levelname)-4s %(message)s')
    client = Client('https://ca252a631c4b437cac81ea0ad3e545ff:d31c83bc53b644138831c7c7d41ba661@sdlog.doordu.com:8205/17', transport=AioHttpTransport)
    config = configparser.ConfigParser()
    config.read('/etc/ddconnector.ini')
    server = Server(config, client)
    server.run()
    
if __name__ == "__main__":
    main()
    
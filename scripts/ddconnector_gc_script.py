import sys
import logging
import time
import socket
from logging.config import fileConfig
import configparser
from functools import partial

import schedule
from raven import Client
from raven_aiohttp import AioHttpTransport


def gc(config):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((config.get('general', 'server_ip'), 
                      config.getint('general', 'listen_port')))
        message = b"eyJjbWQiOiAiZ2MifQ==*"

        sock.sendall(message)
        response = sock.recv(2046).decode("utf-8")
        logging.info(response)
    except Exception:
        logging.info("连接服务端失败！")
    finally:
        sock.close()   
    


def main():
    config_file = '/etc/ddconnector.ini'
    
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    
    fileConfig(config_file)
    
    client = Client('https://ca252a631c4b437cac81ea0ad3e545ff:d31c83bc53b644138831c7c7d41ba661@sdlog.doordu.com:8205/17', transport=AioHttpTransport)
    config = configparser.ConfigParser()
    config.read(config_file)
    
    schedule.every(config.getint('general', 'gc_duration')).minutes.do(partial(gc, config))
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    
if __name__ == "__main__":
    main()
    
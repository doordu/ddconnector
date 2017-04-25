import logging
import configparser

from ddconnector.server import Server


def main():
    logging.basicConfig(filename="ddconnector.log", 
                        level=logging.INFO,
                        format='%(asctime)s %(name)-4s %(levelname)-4s %(message)s')
    config = configparser.ConfigParser()
    config.read('/etc/ddconnector.ini')
    server = Server(config)
    server.run()
    
if __name__ == "__main__":
    main()
    
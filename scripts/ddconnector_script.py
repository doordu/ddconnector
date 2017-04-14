import logging

from ddconnector.server import Server

logger = logging.getLogger(__name__)

def main():
    server = Server()
    server.run()
    
if __name__ == "__main__":
    main()
    
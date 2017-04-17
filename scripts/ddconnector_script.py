import logging

from ddconnector.server import Server


def main():
    logging.basicConfig(filename="ddconnector.log", 
                        level=logging.INFO,
                        format='%(asctime)s %(name)-4s %(levelname)-4s %(message)s')
    server = Server()
    server.run()
    
if __name__ == "__main__":
    main()
    
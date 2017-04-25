import logging
import uvloop

from ddconnector.protocol import Protocol

class Server:
    def __init__(self, config, server_address=('0.0.0.0', 9501)):
        self.config = config
        self.server_address = server_address
        self.transports = {}
        self.loop = uvloop.new_event_loop()
        factory = self.loop.create_server(
                    lambda:Protocol(self),  *server_address)
        self.server = self.loop.run_until_complete(factory)
        
        
    def run(self):
        logging.info("Staring up on {} port {}".format(
                        *self.server_address))
        try:
            self.loop.run_forever()
        finally:
            self.server.close()
            self.loop.run_until_complete(self.server.wait_closed())
            self.loop.close()
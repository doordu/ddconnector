import asyncio

DELIMITER = b'\r\n'

class Protocol(asyncio.Protocol):
    _buffer = b''
    
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
    
    def data_received(self, data):
        self._buffer += data
        
        while True:
            try:
                line, self._buffer = self._buffer.split(
                    DELIMITER, 1)
            except Exception as e:
                break
            else:
                self.message_received(line)
                
    def message_received(self, msg):
        print(msg)
        
    def connection_lost(self, error):
        if error:
            print("Error: {}".format(error))
        else:
            print("Closing")
            
    def eof_received(self):
        print("Received EOF")
        if self.transport.can_write_eof():
            self.transport.write_eof()
                
    
        
        
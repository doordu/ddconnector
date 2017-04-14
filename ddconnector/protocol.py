import asyncio
import json
import logging

from ddconnector.decoder import decode
from ddconnector.exceptions import (DecodeException, 
                                    UnkownCommandException,
                                    FormatException)
from ddconnector.processors import processors

DELIMITER = b'*'

class Protocol(asyncio.Protocol):
    _buffer = b''
    
    def connection_made(self, transport):
        self.transport = transport
        self.logger = logging.getLogger(__name__)
        #self.address = transport.get_extra_info('peername')
    
    def data_received(self, data):
        '''
        收到包，使用DELIMITER(*)拆包
        :param data:
        '''
        self._buffer += data
        
        while True:
            try:
                line, self._buffer = self._buffer.split(
                    DELIMITER, 1)
            except ValueError:
                break
            else:
                self.message_received(line)
    
    def message_received(self, msg):
        '''
        拆包后进行解码，并找到cmd对应的processor
        :param msg:
        '''
        try:
            msg = decode(msg)
            processor = processors[msg['cmd']]
            p = processor()
            p.process(self.transport, msg)
        except DecodeException:
            self.logger.error("%r => base64解码失败！", msg)
        except UnkownCommandException:
            self.logger.error("%r => 未知命令！", msg)
        except FormatException:
            self.logger.error("%r => 数据结构错误！", msg)
            
            
    def connection_lost(self, error):
        if error:
            print("Error: {}".format(error))
        else:
            print("Closing")
            
    def eof_received(self):
        print("Received EOF")
        if self.transport.can_write_eof():
            self.transport.write_eof()
                
    
        
        
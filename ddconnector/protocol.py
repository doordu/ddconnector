import asyncio
import logging

from ddconnector.decoder import decode, encode
from ddconnector.exceptions import (DecodeException, 
                                    UnkownCommandException,
                                    FormatException)
from ddconnector.processors import processors

DELIMITER = b'*'

class Protocol(asyncio.Protocol):
    __slots__ = ('server', 'guid', '_buffer', 'transport', 'last_time')
    
    def __init__(self, server):
        self.server = server
        self.guid = None
        self.address = None
        self._buffer = b''
        self.last_time = 0
    
    def connection_made(self, transport):
        self.transport = transport
    
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
            processor = processors.get(msg['cmd']) or processors.get('magic')
            self.server.loop.create_task(processor(self, msg))
        except DecodeException:
            logging.error("%r => base64解码失败！", msg)
            self.server.raven.captureException()
            self.transport.close()
            
#    def connection_lost(self, error):
#        logging.info("关闭连接！guid: %s, %s", self.guid, self.transport.get_extra_info('peername'))
#         try:
#             del self.server.doors[self.guid]
#         except KeyError:
#             pass
#         if error:
#             logging.info("异常: {}".format(error))
#         else:
#             logging.info("关闭连接")
            
    def eof_received(self):
        if self.transport.can_write_eof():
            self.transport.write_eof()
                
    
        
        
import asyncio
import logging

from ddconnector.decoder import decode, encode
from ddconnector.exceptions import (DecodeException, 
                                    UnkownCommandException,
                                    FormatException)
from ddconnector.processors import processors

DELIMITER = b'*'

class Protocol(asyncio.Protocol):
    __slots__ = ('server', 'guid', '_buffer', 'transport')
    
    def __init__(self, server):
        self.server = server
        self.guid = ''
        self._buffer = b''
    
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
            processor = processors[msg['cmd']]
            task = self.server.loop.create_task(processor(self, msg))
            asyncio.ensure_future(task)
        except DecodeException:
            logging.error("%r => base64解码失败！", msg)
        except UnkownCommandException:
            logging.error("%r => 未知命令！", msg)
        except FormatException:
            logging.error("%r => 数据结构错误！", msg)
        except KeyError:
            logging.error("%r => 未知命令！", msg)
            
    def connection_lost(self, error):
        logging.info("收到断开连接请求！guid: %s", self.guid)
        try:
            del self.server.transports[self.guid]
        except KeyError:
            pass
        if error:
            logging.error("异常: {}".format(error))
        else:
            logging.info("关闭连接")
        super().connection_lost(error)
            
    def eof_received(self):
        if self.transport.can_write_eof():
            self.transport.write_eof()
                
    
        
        
import logging

from ddconnector.processors.base import Processor
from ddconnector.exceptions import FormatException

class Hearbeat(Processor):
    '''
    处理心跳
    '''
    def __init__(self):
        # TODO 连接redis
        pass
        
    def process(self, transport, msg):
        '''
        将transport客户端信息更新至redis
        :param transport: 客户端连接
        :param msg: 发送的消息
        '''
        try:
            guid = msg['guid']
            version = msg['version']
            address = transport.get_extra_info('peername')
            print("guid: %s, address: %s" % (guid, address))
        except IndexError:
            raise FormatException()

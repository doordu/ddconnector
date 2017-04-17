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
        
    def process(self, protocol, msg):
        '''
        将transport客户端信息更新至redis
        :param protocol: Protocol实例
        :param msg: 发送的消息
        '''
        try:
            guid = msg['guid']
            version = msg['version']
            address = protocol.transport.get_extra_info('peername')
            protocol.transports[guid] = protocol.transport
            protocol.guid = guid
            logging.info("guid: %s, address: %s" % (guid, address))
        except IndexError:
            raise FormatException()

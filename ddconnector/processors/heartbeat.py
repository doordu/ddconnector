import logging

import aioredis

from ddconnector.decoder import encode
from ddconnector.exceptions import FormatException

        
async def heartbeat(protocol, msg):
    '''
    将transport客户端信息更新至redis
    :param protocol: Protocol实例
    :param msg: 发送的消息
    '''
    try:
        guid = msg['guid']
        version = msg['version']
        address = protocol.transport.get_extra_info('peername')
        protocol.server.transports[guid] = protocol.transport
        protocol.guid = guid
        logging.info("guid: %s, address: %s" % (guid, address))
        redis = await aioredis.create_redis(('localhost', 6379), loop=protocol.server.loop)
        redis_key = 'tcp_server_{}_heart_beat'.format(guid)
        await redis.set(redis_key, '')
        redis.close()
        await redis.wait_closed()
        response = {'request_id': guid, 
                    'cmd': 'heart_beat'}
        response = encode(response)
        protocol.transport.write(response)
    except IndexError:
        raise FormatException()
    
    
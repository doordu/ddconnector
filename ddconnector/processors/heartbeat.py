import logging
import json
import asyncio
import aioredis

from ddconnector.decoder import encode
from ddconnector.exceptions import FormatException
        

@asyncio.coroutine
def connect(protocol):
    if protocol.server.redis_pool is None:
        protocol.server.redis_pool = yield from aioredis.create_pool(
            (protocol.server.config['redis']['host'], protocol.server.config['redis']['port']), 
            password=protocol.server.config['redis']['password'], 
            loop=protocol.server.loop)
    return protocol.server.redis_pool
        
        
@asyncio.coroutine
def heartbeat(protocol, msg):
    '''
    将transport客户端信息更新至redis
    :param protocol: Protocol实例
    :param msg: 发送的消息
    '''
    try:
        guid = msg['guid']
        version = msg['version']
        msg['fd'] = 0
        msg['server_host'] = protocol.server.config['general']['server_ip']
        msg['server_port'] = protocol.server.config['general']['listen_port']
        address = protocol.transport.get_extra_info('peername')
        protocol.server.transports[guid] = protocol.transport
        protocol.guid = guid
        logging.info("收到心跳信息！guid: %s, address: %s" % (guid, address))
        pool = yield from connect(protocol)
        redis_key = '{}_heart_beta'.format(guid)
        with (yield from pool) as conn:
            yield from conn.set(redis_key, json.dumps(msg), expire=int(protocol.server.config['general']['heartbeat_expires']))
        
        response = {'request_id': guid, 
                    'cmd': 'heart_beat'}
        response = encode(response)
        protocol.transport.write(response)
    except IndexError:
        raise FormatException()
    
    
import logging
import json
import asyncio
import time

import aioredis

from ddconnector.decoder import encode
from ddconnector.exceptions import FormatException
        

@asyncio.coroutine
def connect(protocol):
    if protocol.server.redis_pool is None:
        protocol.server.redis_pool = yield from aioredis.create_pool(
            (protocol.server.config['redis']['host'], protocol.server.config.getint('redis', 'port')), 
            password=protocol.server.config['redis']['password'], 
            minsize=protocol.server.config.getint('redis', 'pool_min_size'),
            maxsize=protocol.server.config.getint('redis', 'pool_max_size'),
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
        msg['server_host'] = protocol.server.config['general']['lan_ip']
        msg['server_port'] = protocol.server.config['general']['listen_port']
        address = protocol.transport.get_extra_info('peername')
        msg['client_host'], msg['client_port'] = address
        
        try:
            # 实验性回收旧连接
            last_protocol = protocol.server.doors[guid]
            if last_protocol != protocol:
                logging.info("回收旧连接！guid: %s, address: %s", guid, last_protocol.transport.get_extra_info('peername'))
                last_protocol.transport.close()
                del protocol.server.doors[guid]
        except Exception:
            pass
        
        protocol.guid = guid
        protocol.last_time = time.time()
        protocol.server.doors[guid] = protocol
        
        #logging.info("收到心跳信息！guid: %s, address: %s" % (guid, address))
        pool = yield from connect(protocol)
        redis_key = '{}_heart_beta'.format(guid)
        with (yield from pool) as conn:
            yield from conn.set(redis_key, json.dumps(msg), expire=protocol.server.config.getint('general', 'heartbeat_expires'))
        response = {'request_id': guid, 
                    'cmd': 'heart_beat'}
        response = encode(response)
        protocol.transport.write(response)
        yield from send_unread_command(protocol, pool, guid)
    except IndexError:
        raise FormatException()

@asyncio.coroutine
def send_unread_command(protocol, pool, guid):
    commands = None
    with (yield from pool) as conn:
        commands = yield from conn.smembers('ddconnector_unread_command_for_' + guid)

    for command in commands:
        logging.info("下发未读指令[%s]！guid: %s", command, guid)
        request_message = {'cmd': command.decode('utf-8'),
                           'request_id': guid,
                           'response_params':
                               {'data': [],
                                'message': '',
                                'success': True,
                                'totalCount': '0'},
                           'response_type': False,
                           'token_id': ''}
        request_message = encode(request_message)
        try:
            protocol.server.doors[guid].transport.write(request_message)
        except KeyError:
            protocol.server.raven.captureException()
            logging.info("guid: %s 不在线，下发指令失败！", guid)






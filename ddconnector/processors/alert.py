import logging
import ujson as json
import asyncio
import time
import urllib
import urllib2

import aioredis

from ddconnector.decoder import encode
from ddconnector.exceptions import FormatException

# 防拆报警处理

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
def alert(protocol, msg):
    '''
    调用后端服务将防拆报警写入数据库并发送到物业管理机
    '''
    try:
        guid = msg['guid']
        version = msg['version']
        address = protocol.transport.get_extra_info('peername')

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

        logging.info("收到防拆报警！guid: %s, address: %s" % (guid, address))
        pool = yield from connect(protocol)
        redis_key = '{}_cmd_alert'.format(guid)
        commands = None
        with (yield from pool) as conn:
            commands = yield from conn.get(redis_key)
        if(commands is None) :
            yield from call_service_alert(protocol, guid)

            with (yield from pool) as conn:
                commands = yield from conn.set(redis_key,time.time(),60)

    except IndexError:
        raise FormatException()

@asyncio.coroutine
def call_service_alert(guid):
    req_url = protocol.server.config['ddservice']['host']+'/dds/door/v1/message/alert'
    req_data = {"access_token":get_access_token(),"timestamp":time.time(),"guid":guid}
    req_data = sorted(data.iteritems(), key=lambda d:d[1], reverse = True)
    req_data_urlencode = urllib.urlencode(req_data)
    req = urllib2.Request(url = req_url,data = req_data_urlencode)
    res_data = urllib2.urlopen(req)
    json_data = res_data.read()
    data = json.loads(json_data)
    return data


def get_access_token():
    redis_key = 'ddconnector_dds_access_token'
    cache_token = None
    pool = yield from connect(protocol)
    with (yield from pool) as conn:
        cache_token = yield from conn.get(redis_key)

    if(cache_token is None):
        req_url = protocol.server.config['ddservice']['host']+'/dds/auth/v1/oauth2/access_token'
        req_data = {"appid":protocol.server.config['ddservice']['appid'],"secret":protocol.server.config['ddservice']['secret']}
        req_data_urlencode = urllib.urlencode(req_data)
        req = urllib2.Request(url = req_url,data = req_data_urlencode)
        res_data = urllib2.urlopen(req)
        json_data = res_data.read()
        data = json.loads(json_data)
        if(data is not None):
            with (yield from pool) as conn:
                commands = yield from conn.set(redis_key,data['data']['access_token'],data['data']['expires_in'])
            return data['data']['access_token'];

    return cache_token





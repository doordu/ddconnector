import logging
import ujson as json
import asyncio
from collections import defaultdict

from ddconnector.decoder import encode


@asyncio.coroutine
def connectsipserver(protocol, msg):
    """
    连接SIP服务器
    """
    if 'isClient' in msg:
        # 下发连接SIP服务器指令
        logging.info("收到下发连接SIP服务器指令请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'connectSipServer',
                           'request_id': msg['guid'],
                           'response_params': 
                                {'data': [json.loads(msg['data'])],
                                 'message': '',
                                 'success': True,
                                 'totalCount': '0'},
                           'response_type': False,
                           'token_id': ''}
        request_message = encode(request_message)
        try:
            protocol.server.doors[msg['guid']].transport.write(request_message)
            protocol.server.waiters[msg['guid']] = protocol
        except KeyError:
            #protocol.server.raven.captureException()
            logging.error("guid: %s 不在线，下发连接SIP服务器指令失败！", msg['guid'])
            response_message = {'cmd': 'connectSipServer', 'status': -1, 'message': '门禁主机不在线'}
            response_message = encode(response_message)
            protocol.transport.write(response_message)
            protocol.transport.close()
    else:
        # 收到门禁回复
        logging.info("收到连接SIP服务器指令回复！guid: %s", msg['guid'])
        response_message = {'cmd': 'connectSipServer',
                            'request_id': msg['guid'],
                            'response_params': {'data': [],
                                                'message': '',
                                                'success': True,
                                                'totalCount': '0'},
                            'response_type': True,
                            'token_id': ''}
        response_message = encode(response_message)
        # 根据之前的门禁guid => [等候者列表]关系进行回包

        try:
            protocol.server.waiters[msg['guid']].transport.write(response_message)
            protocol.server.waiters[msg['guid']].transport.close()
            del protocol.server.waiters[msg['guid']]
        except KeyError:
            logging.info("黑白名单回复之前发送请求关联关系不存在！guid: %s", msg['guid'])
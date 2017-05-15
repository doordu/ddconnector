import logging
import ujson
import asyncio
from collections import defaultdict

from ddconnector.decoder import encode


@asyncio.coroutine
def cardnew(protocol, msg):
    """
    处理开门
    """
    if 'isClient' in msg:
        # 下发黑白名单
        logging.info("收到下发黑白名单请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'cardNew',
                           'request_id': msg['guid'],
                           'response_params': 
                                {'data': [ujson.loads(msg['data'])],
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
            logging.error("guid: %s 不在线，下发黑白名单指令失败！", msg['guid'])
            response_message = {'cmd': 'cardNew', 'status': -1, 'message': '门禁主机不在线'}
            response_message = encode(response_message)
            protocol.transport.write(response_message)
            protocol.transport.close()
    else:
        # 收到门禁开门回复
        logging.info("收到下发黑白名单回复！guid: %s", msg['guid'])
        response_message = {'cmd': 'cardNew',
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
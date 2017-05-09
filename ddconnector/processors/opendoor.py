import logging
import json
import asyncio

from ddconnector.decoder import encode

@asyncio.coroutine
def opendoor(protocol, msg):
    """
    处理开门
    """
    if 'isClient' in msg:
        # 发起开门
        logging.info("收到开门请求！guid: %s, %s", msg['guid'], protocol.transport.get_extra_info('peername'))
        request_message = {'cmd': 'open_door',
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
            # 建立guid => [等待回复者列表]建立关系，方便门禁返回时回复
            protocol.server.waiters[msg['guid']] = protocol
        except KeyError:
            logging.info("guid: %s 不在线，下发命令开门指令失败！", msg['guid'])
            response_message = {'cmd': 'open_door', 'status': -1, 'message': '门禁主机不在线'}
            response_message = encode(response_message)
            protocol.transport.write(response_message)
            protocol.transport.close()
    else:
        # 收到门禁开门回复
        logging.info("收到开门回复！guid: %s", msg['guid'])
        response_message = {'cmd': 'open_door',
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
            logging.info("开门回复之前发送请求关联关系不存在！guid: %s", msg['guid'])

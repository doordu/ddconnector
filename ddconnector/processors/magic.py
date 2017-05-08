import logging
import json
import asyncio

from ddconnector.decoder import encode


@asyncio.coroutine
def magic(protocol, msg):
    """
    处理通用指令
    """
    if 'isClient' in msg:
        #　下发指令
        logging.info("收到[%s]请求！guid: %s", msg['cmd'], msg['guid'])
        request_message = {'cmd': msg['cmd'],
                           'request_id': msg['guid'],
                           'response_params': 
                                {'data': [json.loads(msg['data'])],
                                 'message': '',
                                 'success': True,
                                 'totalCount': '0'},
                           'response_type': False,
                           'token_id': ''}
        request_message = encode(request_message)
        protocol.transport.close()
        try:
            protocol.server.protocols[msg['guid']].transport.write(request_message)
        except KeyError:
            protocol.server.raven.captureException()
            logging.info("guid: %s 不在线，下发命令开门指令失败！", msg['guid'])
    else:
        # 收到回复
        logging.info("收到[%s]回复！guid: %s", msg['cmd'], msg['guid'])
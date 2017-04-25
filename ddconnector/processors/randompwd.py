import logging
import json
from collections import defaultdict

from ddconnector.decoder import encode

async def randompwd(protocol, msg):
    """
    处理开门
    """
    if 'isClient' in msg:
        # 发起开门
        logging.info("收到下发开门密码请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'randomPwd',
                           'request_id': msg['guid'],
                           'response_params': 
                                {'data': [json.loads(msg['data'])],
                                 'message': '',
                                 'success': True,
                                 'totalCount': '0'},
                           'response_type': False,
                           'token_id': ''}
        request_message = encode(request_message)
        protocol.close()
        protocol.server.transports[msg['guid']].write(request_message)
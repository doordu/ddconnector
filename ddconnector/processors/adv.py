import logging
import json
from collections import defaultdict

from ddconnector.decoder import encode


async def adv(protocol, msg):
    """
    门禁主黑白名单更新
    """
    if 'isClient' in msg:
        logging.info("收到更改更新请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'advertisement',
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
    
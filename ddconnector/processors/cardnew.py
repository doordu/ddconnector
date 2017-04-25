import logging
import json
from collections import defaultdict

from ddconnector.decoder import encode


async def cardnew(protocol, msg):
    """
    门禁主黑白名单更新
    """
    if 'isClient' in msg:
        logging.info("收到黑白名单更新请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'cardNew',
                           'request_id': msg['guid'],
                           'response_params': 
                                {'data': [json.loads(msg['data'])],
                                 'message': '',
                                 'success': True,
                                 'totalCount': '0'},
                           'response_type': False,
                           'token_id': ''}
        request_message = encode(request_message)
        protocol.server.transports[msg['guid']].write(request_message)
    
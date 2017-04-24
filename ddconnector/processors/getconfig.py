import logging
import json

from ddconnector.decoder import encode


async def getconfig(protocol, msg):
    """
    下发配置信息
    """
    if 'isClient' in msg:
        logging.info("收到下发配置请求！guid: %s", msg['guid'])
        request_message = {'cmd': 'get_config',
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
    
        

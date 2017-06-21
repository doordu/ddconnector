import logging
import time
import asyncio
from urllib.parse import urljoin

import aiohttp

"""
防拆报警
reference: https://aiohttp.readthedocs.io/en/stable/client.html
"""

ALERT_FREQUENTLY = 60
ACCESS_TOKEN = None


async def get_access_token(protocol):
    global ACCESS_TOKEN
    if ACCESS_TOKEN is None:
        access_token_url = urljoin(protocol.server.config['ddservice']['host'], '/dds/auth/v1/oauth2/access_token')
        access_token_params = {"appid": protocol.server.config['ddservice']['appid'],
                               "secret": protocol.server.config['ddservice']['secret']}
        async with aiohttp.ClientSession() as session:
            async with session.post(access_token_url, params=access_token_params, timeout=10) as resp:
                #logging.info("获取access_token，状态码：%s ", resp.status)
                result = await resp.json()
                #logging.info("获取access_token，结果：%s ", await resp.text())
                try:
                    ACCESS_TOKEN = result['data']['access_token']
                    #logging.info("ACCESS_TOKEN：%s ", ACCESS_TOKEN)
                except IndexError:
                    pass
            
                
async def alert_to_service(protocol, guid):
    global ACCESS_TOKEN
    alert_url = urljoin(protocol.server.config['ddservice']['host'], '/dds/door/v1/message/alert')
    #logging.info("alert_url：%s ", alert_url)
    alert_params = {"guid": guid, "access_token": ACCESS_TOKEN,"timestamp":int(time.time())}
    #logging.info("alert_params：%s ", alert_params)
    async with aiohttp.ClientSession() as session:
        async with session.post(alert_url, params=alert_params, timeout=10) as resp:
            #logging.info("发送防拆报警到服务，状态码：%s ", resp.status)
            result = await resp.json()
            #logging.info("发送防拆报警到服务，结果：%s ", await resp.text())
            if resp.status == 400 and result['code'] == 10501:
                # ACCESS_TOKEN过期
                ACCESS_TOKEN = None
                await get_access_token(protocol)
                await alert_to_service(protocol, alert_time, guid)



async def alert(protocol, msg):
    guid = msg['guid']
    alert_time = time.time()
    if alert_time - protocol.alert_time > ALERT_FREQUENTLY:
        logging.info("收到报警信息！guid: %s，达到上报时间", guid)
        # 超过60s报警
        protocol.alert_time = alert_time
        await get_access_token(protocol)
        await alert_to_service(protocol, guid)
    else:
        logging.info("收到报警信息！guid: %s，未达到上报时间", guid)


        


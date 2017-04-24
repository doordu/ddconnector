from .heartbeat import heartbeat
from .opendoor import opendoor
from .getconfig import getconfig
from .reboot import reboot


processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'get_config': getconfig,                        # 配置
    'reboot': reboot,                               # 重启
}



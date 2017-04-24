from .heartbeat import heartbeat
from .opendoor import opendoor
from .getconfig import getconfig
from .reboot import reboot
from .softupdate import softupdate
from .randompwd import randompwd


processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'get_config': getconfig,                        # 配置
    'reboot': reboot,                               # 重启
    'softUpdate': softupdate,                       # 应用更新
    'randomPwd': randompwd,                         # 开门密码
}



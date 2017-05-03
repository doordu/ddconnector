from .heartbeat import heartbeat
from .opendoor import opendoor
from .cardnew import cardnew
from .debug import debug
from .magic import magic

processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'cardNew': cardnew,                             # 黑白名单
    'debug': debug,                                 # 日志
    'magic': magic                                  # 通用
}



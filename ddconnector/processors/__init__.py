from .heartbeat import heartbeat
from .opendoor import opendoor
from .debug import debug
from .magic import magic

processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'debug': debug,                                 # 日志
    'magic': magic                                  # 通用
}



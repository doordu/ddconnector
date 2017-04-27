from .heartbeat import heartbeat
from .opendoor import opendoor
from .magic import magic

processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'magic': magic                                  # 通用
}



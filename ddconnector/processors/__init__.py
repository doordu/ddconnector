from .heartbeat import heartbeat
from .opendoor import opendoor
from .cardnew import cardnew
from .debug import debug
from .magic import magic
from .total import total
from .gc import gc

processors = {
    'heart_beat': heartbeat,                        # 心跳
    'open_door': opendoor,                          # 开门
    'cardNew': cardnew,                             # 黑白名单
    'debug': debug,                                 # 日志
    'total': total,                                 # 统计连接数
    'gc': gc,                                       # 连接回收
    'magic': magic                                  # 通用
}



from .heartbeat import heartbeat
from .opendoor import opendoor


processors = {
    'heart_beat': heartbeat,
    'open_door': opendoor
}



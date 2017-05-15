import unittest
from unittest.mock import Mock, patch

from ddconnector.protocol import Protocol
from ddconnector.decoder import decode


class TestProtocol(unittest.TestCase):
    def setUp(self):
        self.transportMock = Mock()
        self.serverMock = Mock()
        self.protocol = Protocol(self.serverMock)
        self.protocol.connection_made(self.transportMock)
        
    @patch('ddconnector.protocol.processors')
    def test_opendoor(self, mock_processors):
        """
        d = {'fd': 0, 'cmd': 'open_door', 'from_id': 0, 'guid': 'DD302WI201512A-1355', 'isClient': True, 'time': '2017-05-09 15:36:08', 'data': '{"room_id": 0}'}
        """
        msg = b'eyJmZCI6IDAsICJjbWQiOiAib3Blbl9kb29yIiwgImZyb21faWQiOiAwLCAiZ3VpZCI6ICJERDMw\nMldJMjAxNTEyQS0xMzU1IiwgImlzQ2xpZW50IjogdHJ1ZSwgInRpbWUiOiAiMjAxNy0wNS0wOSAx\nNTozNjowOCIsICJkYXRhIjogIntcInJvb21faWRcIjogMH0ifQ==\n*'
        self.protocol.data_received(msg)
        
        msg2 = decode(msg)
        # 确定创建了新的task处理开门
        self.serverMock.loop.create_task.assert_called()
        
        # 调用processor为开门
        mock_processors.get.assert_called_with('open_door')
        
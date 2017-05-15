import unittest
from unittest.mock import Mock

from ddconnector.server import Server


class TestServer(unittest.TestCase):
    def setUp(self):
        print("setUp()...")
        
    def test_server(self):
        from configparser import ConfigParser
        config = ConfigParser()
        config['general'] = {
            'server_ip': '0.0.0.0',
            'listen_port': 9501
        }
        loop = Mock()
        
        raven = Mock()
        server = Server(config, raven)
        server.loop = loop
        server.run()
        loop.run_forever.assert_called()
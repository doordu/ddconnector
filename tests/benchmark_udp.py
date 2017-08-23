import asyncio
import json
import base64

class EchoClientProtocol:
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message)

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()


loop = asyncio.get_event_loop()
d = {"guid":"testzz20170609","cmd":"heart_beat","version":"5.8.000.0"}
message = json.dumps(d)
message = base64.encodebytes(message.encode('utf_8')) + b'*'
connect = loop.create_datagram_endpoint(
    lambda: EchoClientProtocol(message, loop),
    remote_addr=('127.0.0.1', 9501))
transport, protocol = loop.run_until_complete(connect)
loop.run_forever()
transport.close()
loop.close()
import socket
import struct

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
s.connect(('localhost', 8000))
s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
s.close()
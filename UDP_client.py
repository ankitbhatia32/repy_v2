import socket 

UDP_IP = '::1'
UDP_PORT = 3001
MESSAGE = 'Hello from the other side'

def udpclientconnect():
  s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

  return s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
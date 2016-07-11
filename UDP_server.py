import socket

UDP_IP = '::1'
UDP_PORT = 3001
#Create a socket

def udpserverconnect():
  s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

  s.bind((UDP_IP,UDP_PORT))

  print "Now you are connected...."

  while True:
    data, addr = s.recvfrom(1024)
    print "Message Received:", data

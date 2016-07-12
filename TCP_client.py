import socket

TCP_IP = "::1" 
TCP_PORT = 5007
Message = 'Hello from the other side'

def tcpclientconnect():
  s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
  s.connect((TCP_IP, TCP_PORT))
  s.sendto(Message, (TCP_IP, TCP_PORT))
  data = s.recv(1024)
  s.close()

  print "Received data:", data

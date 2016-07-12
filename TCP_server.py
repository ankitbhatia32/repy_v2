import socket


TCP_IP = "::1" 
TCP_PORT = 5007

def tcpserverconnect():
  s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
  s.bind((TCP_IP, TCP_PORT))
  s.listen(1)

  print "Now Listening...."

  conn, addr = s.accept()
  print 'Connection Address', addr

  while True:
    data = conn.recv(1024)
    if not data: break 
    print 'Received data:' , data
    conn.send(data) 
  conn.close()
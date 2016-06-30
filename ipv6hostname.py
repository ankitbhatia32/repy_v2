import socket

def getAddrip6(input1):
  #return socket.getaddrinfo(input1, None, socket.AF_INET6)
  return socket.getaddrinfo(input1, None)

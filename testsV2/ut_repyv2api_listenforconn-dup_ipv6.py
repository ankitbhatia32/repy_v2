"""
This unit test checks that we get a AlreadyListeningError if you
try to listen on an IP/Port pair that is already in use.
"""
#pragma repy restrictions.fixed

ip = "::1"
port = 12345

listen_sock = listenforconnection_ipv6(ip, port)

try:
  listen_sock_2 = listenforconnection_ipv6(ip, port)
  log("Should get AlreadyListeningError!",'\n')
except AlreadyListeningError:
  pass


"""
Check that open after listen is forbidden.
"""
#pragma repy restrictions.fixed

localip = "::1"
localport = 12345
remoteip = "::1"
remoteport = 43214
timeout = 1.0

tcpserversocket = listenforconnection_ipv6(localip, localport)

try:
  # Even though I'm connecting to something invalid, the AlreadyListeningError
  # has precedence
  openconnection_ipv6(remoteip, remoteport, localip,localport, timeout)
except AlreadyListeningError:
  pass
else:
  log("Did not get AlreadyListeningError when connecting after a listen",'\n')

tcpserversocket.close()

"""
Check what happens with send and close
"""
#pragma repy restrictions.twoports

localip = "::1"
localport = 12345
targetip = "::1"
targetport = 12346
timeout = 1.0


tcpserversocket = listenforconnection_ipv6(targetip, targetport)

conn = openconnection_ipv6(targetip, targetport, localip, localport, timeout)


(ip, port, serverconn) = tcpserversocket.getconnection()

assert(ip == localip)
assert(port == localport)

conn.close()
try:
  amountsent = conn.send('hi')
except SocketClosedLocal:
  pass
else:
  log("Should get an error if we closed the socket locally",'\n')


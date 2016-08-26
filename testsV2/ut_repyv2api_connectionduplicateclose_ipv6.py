"""
Check what happens with duplicates close
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

# first call should be True, second is False...
assert(conn.close() == True)
assert(conn.close() == False)

# first call should be True, second is False...
assert(serverconn.close() == True)
assert(serverconn.close() == False)



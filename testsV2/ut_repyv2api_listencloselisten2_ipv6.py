"""
Check that I can receive connections after stopping listening even with
connections going on...
"""
#pragma repy restrictions.twoports

localip = "::1"
localport = 12345
targetip = "::1"
targetport = 12346
timeout = 1.0


tcpserversocket = listenforconnection_ipv6(targetip, targetport)

# Connect...
conn = openconnection_ipv6(targetip, targetport, localip, localport, timeout)

conn.close()

# stop listening...
tcpserversocket.close()


# try to listen again and reconnect
tcpserversocket = listenforconnection_ipv6(targetip, targetport)
conn = openconnection_ipv6(targetip, targetport, localip, localport, timeout)

(ip, port, serverconn) = tcpserversocket.getconnection()

assert(ip == localip)
assert(port == localport)


conn.close()
serverconn.close()
tcpserversocket.close()

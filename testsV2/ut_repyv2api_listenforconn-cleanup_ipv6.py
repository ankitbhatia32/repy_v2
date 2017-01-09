"""
This unit test checks that we do not get a DuplicateTupleError if you
try to listen on an IP/Port pair that is was in use, but was
closed.
"""
#pragma repy restrictions.fixed

ip = "::1"
port = 12345

listen_sock = listenforconnection_ipv6(ip, port)
listen_sock.close() # Stop

listen_sock_2 = listenforconnection_ipv6(ip, port)
listen_sock_2.close()


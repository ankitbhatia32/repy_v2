"""
This unit test checks that we get a ResourceForbiddenError
when providing bad ports to listenforconnection.
"""
#pragma repy

ip = "::1"

def tryit(port):
  try:
    listenforconnection_ipv6(ip,port)
    log("Bad combination worked! IP:"+str(ip)+" Port: "+str(port),'\n')
  except ResourceForbiddenError:
    pass

# Try some bad combos
tryit(2345)
tryit(80)
tryit(22)
tryit(1000)
tryit(10000)



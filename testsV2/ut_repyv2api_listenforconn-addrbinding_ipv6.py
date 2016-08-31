"""
This unit test checks that we get a AddressBindingError
when providing bad IP's to listenforconnection.
"""
#pragma repy restrictions.fixed

PORT = 12345

def tryit(ip):
  try:
    listenforconnection_ipv6(ip,PORT)
    log("Bad combination worked! IP:"+str(ip)+" Port: "+str(port),'\n')
  except AddressBindingError:
    pass

# Try some bad combos
tryit("2404:6800:4009:806::200e")
tryit("2001:4998:58:c02::a9")
tryit("2607:f6d0:0:925a::ab43:d7c8")



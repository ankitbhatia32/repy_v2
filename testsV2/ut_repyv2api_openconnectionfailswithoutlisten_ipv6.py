"""
Check that connecting where there isn't a listener will give the appropriate
exception
"""
#pragma repy restrictions.fixed

localip = "::1"
localport = 12345
remoteip = "::1"
remoteport = 43214
timeout = 1.0

try:
  openconnection_ipv6(remoteip, remoteport, localip,localport, timeout)
except ConnectionRefusedError:
  pass
else:
  log("Did not get ConnectionRefusedError connecting to a non-existent listener.",'\n')



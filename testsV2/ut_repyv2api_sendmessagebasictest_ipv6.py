"""
This unit test checks the sendmessage() API call.
"""

#pragma repy
#pragma repy restrictions.twoports

s = listenformessage_ipv6('::1', 12345)

data = "HI"*8

sendmessage('::1', 12345, data, '::1', 12346)

(rip, rport, mess) = s.getmessage()

s.close()

if mess != data:
  log("Mismatch!",'\n')

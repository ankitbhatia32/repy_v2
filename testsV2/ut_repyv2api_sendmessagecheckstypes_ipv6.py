"""
This unit test checks the sendmessage() API call.
"""

#pragma repy
#pragma repy restrictions.twoports


# Check listenformessage() typechecks
try:
  s = listenformessage_ipv6(5, 12345)
except RepyException:
  pass
else:
  log('listenformessage shouldn\'t allow invalid ip/port types','\n')

try:
  s = listenformessage_ipv6('::1', "str")
except RepyException:
  pass
else:
  log('listenformessage shouldn\'t allow invalid ip/port types','\n')

s = listenformessage_ipv6('::1', 12345)

data = "HI"*8

# Check sendmessage() typechecks
for attempt in [\
    (2, 12345, data, '::1', 12346), \
    ('::1', "str", data, '::1', 12346), \
    ('::1', 12345, 6, '::1', 12346), \
    ('::1', 12345, data, 6, 12346), \
    ('::1', 12345, data, '::1', "str")]:
  try:
    sendmessage_ipv6(attempt[0], attempt[1], attempt[2], attempt[3], attempt[4])
    (rip, rport, mess) = s.getmessage()
  except RepyException:
    pass
  else:
    log("sendmessage shouldn't allow invalid types",'\n')

s.close()

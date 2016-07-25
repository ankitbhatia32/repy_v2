import socket 

import select 

socket.getattr = getattr
socket.setattr = setattr

import threading

threading.hasattr = hasattr

import hashexit
import nonportable 
import tracebackrepy
import nanny
import idhelper
import time
import errno
import repy_constants
from exception_hierarchy import *


_BOUND_SOCKETS = {}

user_ip_interface_preferences_ipv6 = False

allow_nonspecifed_ips_ipv6 = True

user_specified_ip_interface_list_ipv6 = []

allowediplist_ipv6 =[]

cachelock = threading.lock()

def ipv6_aadress_support():
  
  if not socket.has_ipv6:
  	raise Exception("IPv6 is not supported")


def _ip_is_allowed_ipv6(ip):
  

  global allowediplist_ipv6
  global user_ip_interface_preferences_ipv6
  global allow_nonspecifed_ips_ipv6

  if not user_ip_interface_preferences_ipv6 or allow_nonspecifed_ips_ipv6:
    return True

  return (ip in allowediplist_ipv6)

def _unique_append(lst, elem):
  if elem not in lst:
  	lst.append(elem)


def update_ip_cache_ipv6():
  global allowediplist_ipv6
  global user_ip_interface_preferences_ipv6
  global user_specified_ip_interface_list_ipv6
  global allow_nonspecified_ips_ipv6

  if not user_ip_interface_preferences_ipv6:
  	return

  cachelock.acquire()

  try:
    allowed_list_ipv6 = []

  	for (is_ip_addr_ipv6, value) in user_specified_ip_interface_list_ipv6:
  	  if is_ip_addr_ipv6:
  	    _unique_append(allowed_list_ipv6, value)

  	  else:
  	  	try:
  	  	  interface_ips = nonportable.os_api.get_interface_ip_addresses(value)
  	  	  for interface_ip in interface_ips:
  	  	  	_unique_append(allowed_list_ipv6, interface_ip)

  	  	  except:
  	  	    pass

  	  bindable_list = []

  	  for ip in allowed_list_ipv6:
  	  	sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
  	  	try:
  	  	  sock.bind((ip,0))
  	  	except:
  	  	  pass
  	  	else:
  	  	  bindable_list.append(ip)
  	  	finally:
  	  	  sock.close()


  	  	_unique_append(bindable_list, '::1')

  	  	allowediplist_ipv6 = bindable_list

  finally:
    cachelock.release()



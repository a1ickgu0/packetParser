#!/usr/bin/env python
import socket
from IPy import IP

def inet2str(inet):
# First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

def pretty(d, indent=0):
    for key, value in d.iteritems():
        print '\t' * indent + str(key)
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print '\t' * (indent+1) + str(value)

# 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8
def is_private_ip(ipaddr):
    ip = IP(ipaddr)
    if ip.iptype() == 'PRIVATE':
        return True
    else:
        return False

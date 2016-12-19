#!/usr/bin/env python

from parser import *

cap_file = 'sample/http-20161214.pcap'

if __name__ == "__main__":
    parser = Parser()
    parser.openfile( cap_file )
    pass

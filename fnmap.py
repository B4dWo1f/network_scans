#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nmap
##### PART 1
nm = nmap.PortScanner()
#results = nm.scan('127.0.0.1', '22,25,80,443')
#print results
#
#print 
#print nm['127.0.0.1']['tcp'][80]
#print 
#print nm.csv()



##################################
results = nm.scan('192.168.6.0/24')
print nm.command_line()
print results

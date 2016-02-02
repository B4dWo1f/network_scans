#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
from random import random
from time import sleep

"""
  Look for alive hosts
"""

folder = '../test/'

for i in range(255):
   twait = 2*random()
   subnet = '192.168.%s.0/24'%(i)
   fname = folder + subnet
   com = 'nmap -sP --scan-delay %s '%(twait)
   com += '%s -oN %s%s.hosts'%(subnet,folder,subnet[0:-5])
   if not os.path.isfile('%s%s.hosts'%(folder,subnet[0:-5])):
      os.system(com)
      tsleep = 3*random()
      print '******************************'
      print '      wait: %s'%(tsleep)
      print '******************************'
      sleep(tsleep)
   else: print 'Skipping:','%s%s.hosts'%(folder,subnet[0:-5])

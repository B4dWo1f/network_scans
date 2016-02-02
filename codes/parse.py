#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from time import sleep
from random import shuffle,random


def deep_scan(ip,OUT='fingerprinting'):
   """
      Deep scan with nmap searching for OS and ports
      Requires root!!!!
   """
   print 'Performing deep scan of:',ip
   com_mkdir = 'mkdir -p %s'%(OUT)
   fname = OUT+'%s'%(ip)
   com_nmap = 'sudo nmap -sT -O -oN %s.out %s'%(fname,ip)
   print '  ',com_mkdir
   print '  ',com_nmap
   os.system(com_mkdir)
   resp = os.system(com_nmap)


def check_scanned(fname):
   """
     Check if the host has been already scanned
   """
   try:
      for line in open(fname):
         if "(1 host up)" in line:
            return True
   except IOError: return False
   return False


fname = '../uam/uam.hosts'
path_out = '../test/'


lines = open(fname,'r').read().splitlines()

IPs = []
for l in lines:
   if 'Nmap scan report for' in l:
      IPs.append(l.split()[-1].replace('(','').replace(')',''))


shuffle(IPs)  # Random order

for ip in IPs:
   ## check if already scanned
   fname = path_out + ip + '.out'
   if not check_scanned(fname):
      deep_scan(ip,OUT=path_out)
      tsleep = 10*random()   # Random waiting time
      print '**************************'
      print '     Waiting %.5fs'%(tsleep)
      print '**************************'
      sleep(tsleep)
   else: print 'skipping:',ip
   if os.path.isfile('STOP'): exit()

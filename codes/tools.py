#!/usr/bin/env python
# -*- coding: UTF-8 -*-



def port(reports,ps=[80,443]):
   """
     Returns all hosts with any of the ports in ps open
   """
   hosts = []
   for R in reports:
      for l in R:
         pass
         #report = ''.join(rep)
         #if '80/tcp    open  http' in report: 
         #   url = fname.split('/')[1].replace('_','.')
         #   print url
         #   os.system('firefox %s &'%(url))
   return hosts

#import os
#
#OUT = 'fingerprinting'
#
#folders = [x[0] for x in os.walk('fingerprinting')]
#
#for f in folders[1:]:
#   fname = f+'/nmap.log'
#   try:
#      rep = open(fname,'r').readlines()
#      for l in rep:
#         if 'Device type' in l:
#            print fname
#            print l
#      #report = ''.join(rep)
#      #if '80/tcp    open  http' in report: 
#      #   url = fname.split('/')[1].replace('_','.')
#      #   print url
#      #   os.system('firefox %s &'%(url))
#   except IOError:
#      pass

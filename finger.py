#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from os import listdir
from os.path import isfile, join
from time import sleep
from random import random,shuffle
import os

def get_useful_files(path='.'):
   """
     Assumes that all the hosts are stored in files "all_X.txt" where X are
     the subnets scanned.
     For now, only C class networks have been scanned: 192.168.X.0/24
   """
   onlyfiles = [ join(path,f) for f in listdir(path) if isfile(join(path,f)) ]
   files = []
   for f in onlyfiles:
      if '.hosts' in f:
         last_line = open(f,'r').readlines()[-1].lstrip().rstrip()
         try:
            last_line = last_line.replace('Nmap done: 256 IP addresses (','')
            #print last_line
            hosts_up = last_line.split('(')[1].split(')')[0]
            hosts_up = int(hosts_up.replace(' hosts up',''))
            if hosts_up > 0: files.append(f)
         except: # ValueError:
            pass
   return files

def extract_IPs(fname):
   """
      Extract up IPs from an exact output of nmap, searching for the string:
                     Nmap scan report for XXX.XXX.XXX.XXX
   """
   #print 'Extracting:',fname
   IPs = []
   lines = open(fname,'r').readlines()
   for l in lines:
      if 'Nmap scan report for' in l:
         ip = l.split()[-1].replace('(','').replace(')','')
         IPs.append(ip)
   return IPs

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
   scanned = False
   try:
      for line in open(fname):
         if "(1 host up)" in line:
            scanned = True
            break
   except IOError:
      scanned = False
   return scanned


if __name__ == '__main__':
   """
     Randomize the order of the IPs to avoid persistent detection
   """
   mypath = '../test/'
   path_out = '../db/'

   ## Get nmap reports from hosts detection stored in mypath
   files = get_useful_files(path=mypath)

   ## Get Ips from each subnetwork
   IPs = []
   for IPfile in files:
      for ip in extract_IPs(IPfile):
         IPs.append(ip)

   ## Randomize order of IP's
   shuffle(IPs)
   for IP in IPs:
      ip = IP.lstrip().rstrip()
      ## check if already scanned
      fname = path_out+ip+'.out'
      if not check_scanned(fname):
         deep_scan(ip,OUT=path_out)
         tsleep = 10*random()   # Random waiting time
         print '**************************'
         print '     Waiting %.5fs'%(tsleep)
         print '**************************'
         sleep(tsleep)
      else:
         print 'skipping:',ip

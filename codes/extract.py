#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from os import listdir
from os.path import isfile, join


class Host():
   def __init__(self,ip='***.***.***.***',alias='****',ports=[],
                     MAC='**:**:**:**:**:**',fabricante='****',
                     dev='****',op_sys='****',hops='****'):
      """
        Initialize class (in case I want to use an empty Host)
      """
      self.ip = ip
      self.alias = alias
      self.ports = ports
      self.MAC = MAC
      self.fabricante = fabricante
      self.dev = dev
      self.op_sys = op_sys
      self.hops = hops
   def __str__(self):
      """
        String to be printed
      """
      msg = '#######################################\n'
      msg += 'Report for: %s\n'%(self.ip)
      msg += 'alias = %s\n'%(self.alias)
      msg += 'Ports:\n'
      for p in self.ports:
         msg += str(p)+'\n'
      msg += self.MAC + ' ' + self.fabricante + '\n'
      msg += 'Device type: %s\n'%(self.dev)
      msg += 'OS: %s\n'%(self.op_sys)
      msg += 'hops: %s\n'%(self.hops)
      return msg

class Port():
   def __init__(self,tupla=(None,None,None,None)):
      self.port = tupla[0]
      self.protocol = tupla[1]
      self.state = tupla[2]
      self.service = tupla[3]
   def __str__(self):
      lista = [self.port+ '/' +self.protocol,self.state,self.service]
      msg = ' '.join(lista)
      return msg #+'\n'


def analyze_host(fname):
   """
     Extract information from an nmap output
   """
   ## Initialize
   ip = '***.***.***.***'       #
   alias = '****'               #  Default values, if those are not found 
   ports = []                   # in the given file
   MAC = '**:**:**:**:**:**'    #
   fabricante = '****'          #
   dev = '****'                 #
   op_sys = '****'              #
   hops = '****'                #
   ## Reading
   lines = open(fname,'r').readlines()
   ports = []
   for li in lines:
      l = li.lstrip().rstrip()
      ip = fname.replace('../db/','').replace('.out','')
      ##  Search for information
      ## alias and/or IP
      if 'Nmap scan report for ' in l:
         alias = l.replace('Nmap scan report for ','').split()[0]
         try:
            ip = l.replace('Nmap scan report for ','').split()[1]
         except IndexError: pass
      ## Ports
      elif ' open ' in l or ' closed ' in l or ' filtered ' in l:
         try:
            port,state,service = l.split()
         except ValueError: continue
         port,protocol = port.split('/')
         ports.append(Port((port,protocol,state,service)))
      ## MAC
      elif 'MAC Address: ' in l:
         MAC = l.replace('MAC Address: ','').split() # TODO maybe only MAC?
         fabricante = ' '.join(MAC[1:])
         MAC = MAC[0]
      ## Devince
      elif 'Device type: ' in l:
         dev = l.replace('Device type: ','')
      ## OS
      elif 'OS details: ' in l: 
      #elif 'Running: ' in l or 'OS CPE: ' in l or 'OS details: ' in l: # TODO
         op_sys = l.replace('OS details: ','')
      ## hops until host
      elif 'Network Distance: ' in l:
         hops = l.replace('Network Distance: ','')
         hops = int(hops.replace(' hops','').replace(' hop',''))
      #else: print l
   return Host(ip,alias,ports,MAC,fabricante,dev,op_sys,hops)


path = '../db/'
onlyfiles = [ join(path,f) for f in listdir(path) if isfile(join(path,f)) ]
hosts = []
for  fname in onlyfiles:
   hosts.append( analyze_host(fname) )

### Testing
#import json
#def dumper(obj):
#   try:
#      return obj.toJSON()
#   except:
#      return obj.__dict__
#with open('data.json', 'w') as outfile:
#    json.dump(hosts, outfile, default=dumper)


### get ports
#for H in hosts:
#   for p in H.ports:
#      if 'http' in str(p): print H

### get OS
#for H in hosts:
#   if 'Linux' in H.op_sys:
#      print 
#      print H.ip
#      for p in H.ports:
#         print p

### hops
#for H in hosts:
#   if H.hops == 1:
#      if H.dev != 'general purpose' and '**' not in H.dev:
#         print H

### get names
#for n in names:
#   try:
#      map(int, n.split('.'))
#   except:
#      if '*' not in n and 'inl-' not in n: print n

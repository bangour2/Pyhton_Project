#!/usr/bin/python3
#import sys
import os
import re

print ("Content-Type: text/plain; charset=UTF-8")
print()

print ("<h1>Hello!</h1>")

for (k,v) in os.environ.items() :
 print (k, v)

print ()
print ("==========================")
print ()

x = os.environ['QUERY_STRING']
print ("Query is ", x)
comps = re.split('&', x)
for c in comps:
    print (c)
    (key, val) = re.split('=', c)
    print (key,'--->',val)

#!/usr/bin/python3
def func(a,b={}):
   b[a]=a
   return b
print (func(3))
print (func(3))
print (func(4))
print (func(5))

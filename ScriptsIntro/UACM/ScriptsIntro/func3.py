#!/usr/bin/python3
def func(a,b = {}):
       b[a]= a
       return b
dic={'x':2,'y':22}
print(func(3))
print(func(4))
print(func(5,dic))
print(func(2))

#!/usr/bin/python3
def promedio(**numeros):
   sum=0
   for n in numeros:
       sum += numeros[n]
   return sum/len(numeros)

dic={'a':1,'b':2,'c':3}
print (promedio(**dic))
print (promedio(a=1,b=2,c=3))

#!/usr/bin/python3
def promedio(**numeros):
   sum=0
   for n in numeros:
       sum += numeros[n]
   return sum/len(numeros)

def  prom (*numeros):
   sum=0
   for n in numeros:
       sum += n 
   return sum/len(numeros)

a=[5,4,3,2,1]
print(prom(*a))

dic={'a':1,'b':2,'c':10.0}
print (promedio(**dic))

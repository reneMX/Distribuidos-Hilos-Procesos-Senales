#!/usr/bin/python3
def  promedio (*numeros):
   sum=0
   for n in numeros:
       sum += n 
   return sum/len(numeros)

print (promedio(5.5,4,3,2,1))

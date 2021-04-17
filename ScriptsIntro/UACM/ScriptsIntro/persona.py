#!/usr/bin/python3
class persona:
   __nombre =" "
   
   def __init__(self,nombre):
      self.nombre = nombre

   def damenombre(self):
      return self.nombre

   def definenombre(self, nombre): 
      self.nombre = nombre

   def __str__ (self):
      return self.nombre 

p = persona("Arnoldo")
print(p)
p.definenombre("Arturo")
print(p);

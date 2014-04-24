class Pointer:
   x=0
   y=0
   originx=-1
   originy=-1

   def __init__(self,x,y,originx=-1,originy=-1):
           self.x = x
           self.y = y
           self.originx = originx
           self.originy = originy


   def printCoordinates(self):
	   print "Pointer: x: " , self.x , " y: ",  self.y


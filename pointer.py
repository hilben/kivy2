class Pointer:
   x=0
   y=0

   def __init__(self, x,y ):
	   self.x = x
	   self.y = y

   def printCoordinates(self):
	   print "Pointer: x: " , self.x , " y: ",  self.y

a = Pointer(10,4)
a.printCoordinates()

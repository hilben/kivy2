import pointer
import logicblock

class Logic:

        data=[]
        size=0
        pointers=[]

        def __init__(self, size,field):
            self.size=size
            self.field = field
            for y in xrange(size):
                self.data.append([])
                for x in xrange(size):
                    self.data[y].append(logicblock.LogicBlock("","e"))

        def isOnField(self,x,y):
            if x >= 0 and x < self.size and y >= 0 and y < self.size:
                return True
            else:
                return False

        def setBlock(self,x,y,block):
            if self.isOnField(x,y):
                self.data[x][y] = block
       
        def getPointerAt(self,x,y):
	    pointers = []
            for p in self.pointers:
		 if p.x == x and p.y == y:
		     pointers.append(p)
            return pointers

        def printBlocks(self):
             printStr = ""
             for y in xrange(self.size):
                 print printStr + "\n"
                 printStr = ""
                 for x in xrange(self.size):
                     printStr = str(printStr) + "\t" + str(self.data[x][y].blocktype)
		     for p in self.getPointerAt(x,y):
	                 printStr += "*"
             print printStr
	     self.printPointer() 
             
        def getBlock(self,x,y):
            if self.isOnField(x,y):
                return self.data[x][y]
            else:
                return logicblock.LogicBlock("","e")

        def canPlacePointer(self,x,y):
           if self.isOnField(x,y):
               if self.data[x][y].blocktype == "e":
                    return False
               else:
                   r = self.field.findRobot()
                   if self.data[x][y].blocktype == "wu":
                       return not self.field.isPassableBlock(r.x,r.y-1)
                   if self.data[x][y].blocktype == "wd":
                       return not self.field.isPassableBlock(r.x,r.y+1)
                   if self.data[x][y].blocktype == "wl":
                       return not self.field.isPassableBlock(r.x-1,r.y)
                   if self.data[x][y].blocktype == "wr":
                       return not self.field.isPassableBlock(r.x+1,r.y)
                   if self.data[x][y].blocktype == "cu":
                       return self.field.isCollectable(r.x,r.y-1)
                   if self.data[x][y].blocktype == "cd":
                       return self.field.isCollectable(r.x,r.y+1)
                   if self.data[x][y].blocktype == "cl":
                       return self.field.isCollectable(r.x-1,r.y)
                   if self.data[x][y].blocktype == "cr":
                       return self.field.isCollectable(r.x+1,r.y) 

                   return True
        

        def performAction(self,curpointer):
	    x = curpointer.x
	    y = curpointer.y

            if self.isOnField(x,y):
                if self.data[x][y].blocktype=="mu":
                    self.field.moveRobotUp()
                if self.data[x][y].blocktype=="md":
                    self.field.moveRobotDown()
                if self.data[x][y].blocktype=="ml":
                    self.field.moveRobotLeft()  
                if self.data[x][y].blocktype=="mr":
                    self.field.moveRobotRight()
                if self.data[x][y].blocktype=="ab":
                    self.data[x][y].blocktype = "a"
		    self.removePointers(x,y,1)
	        elif self.data[x][y].blocktype=="a":
		    for i in self.find("ab"):
	                self.data[i.x][i.y].blocktype = "a"
	            self.data[x][y].blocktype = "ab"
		    self.removePointers(x,y,1)
		if self.data[x][y].blocktype == "z" and curpointer.originx != -1:
                    zx = x + 2 * (x-curpointer.originx)
		    zy = y + 2 * (y-curpointer.originy)
		    print "ZZZZZZZZZZZZZZ"
		    #self.removePointers(x,y)
		    print "z: " + str(zx) + " " + str(zy)
		    if self.isOnField(zx,zy) and  self.canPlacePointer(zx,zy):
			self.pointers.append(pointer.Pointer(zx,zy,-1,-1))
		        print "put z on field"	


	def find(self,fieldtype):
             foundfields = []
             for y in xrange(self.size):
                 for x in xrange(self.size):
                     if self.data[x][y].blocktype == fieldtype:
                         ftype = pointer.Pointer(x,y)
                         foundfields.append(ftype)
			 print "found " + fieldtype + " at " + str(ftype.x) + " " + str(ftype.y)
             return foundfields

        def printPointer(self):
	    printStr = ""
            for p in self.pointers:
                printStr +=  "[p: x:" + str(p.x) + " y:" + str(p.y) + "]"
	    print printStr


        def reset(self):
	    print "reset logic..."
            self.pointers = []
	    for s in self.find("ab"):
                self.data[s.x][s.y].blocktype = "a"

        def start(self):
	    self.reset()
            for s in self.find("s"):
                self.pointers.append(pointer.Pointer(s.x,s.y))
            
	def removePointers(self,x,y,maxNumber=-1):
	    print "remove p ", str(x), str(y)
	    removes = []
	    for p in self.pointers:
                if p.x == x and p.y == y:
		    removes.append(p)
            currentNumber = maxNumber 
	    for p in removes:
		if currentNumber != 0:
		    currentNumber -= 1
                    self.pointers.remove(p)

        def doIteration(self):
             
            appendPointers = []
            removePointers = []
           
	   
            for p in self.pointers:
                self.performAction(p)
	    for p in self.pointers:
                removePointers.append(p)
                if self.canPlacePointer(p.x,p.y-1) and not (p.originx == p.x and p.originy == p.y-1):
                    appendPointers.append(pointer.Pointer(p.x,p.y-1,p.x,p.y))
                if self.canPlacePointer(p.x,p.y+1) and not (p.originx == p.x and p.originy == p.y+1):
                    appendPointers.append(pointer.Pointer(p.x,p.y+1,p.x,p.y))
                if self.canPlacePointer(p.x-1,p.y) and not (p.originx == p.x-1 and p.originy == p.y):
                    appendPointers.append(pointer.Pointer(p.x-1,p.y,p.x,p.y))
                if self.canPlacePointer(p.x+1,p.y) and not (p.originx == p.x+1 and p.originy == p.y):
                    appendPointers.append(pointer.Pointer(p.x+1,p.y,p.x,p.y))
           
            for p in removePointers:
                self.pointers.remove(p)

            for p in appendPointers:
                self.pointers.append(p)

            
            for s in self.find("ab"):
                self.pointers.append(pointer.Pointer(s.x,s.y))


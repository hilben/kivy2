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
                    self.data[y].append(logicblock.LogicBlock("","empty"))

        def isOnField(self,x,y):
            if x >= 0 and x < self.size and y >= 0 and y < self.size:
                return True
            else:
                return False

        def setBlock(self,x,y,block):
            if self.isOnField(x,y):
                self.data[x][y] = block

        def printBlocks(self):
             printStr = ""
             for y in xrange(self.size):
                 print printStr + "\n"
                 printStr = ""
                 for x in xrange(self.size):
                     printStr = str(printStr) + "\t" + str(self.data[x][y].blocktype)
             self.printPointer() 
             
        def getBlock(self,x,y):
            if self.isOnField(x,y):
                return self.data[x][y]
            else:
                return logicblock.LogicBlock("","empty")

        def canPlacePointer(self,x,y):
           if self.isOnField(x,y):
               if self.data[x][y].blocktype == "empty":
                    return False
               else:
                   return True
        
        def performAction(self,x,y):
            if self.isOnField(x,y):
                if self.data[x][y].blocktype=="moveup":
                    self.field.moveRobotUp()
                if self.data[x][y].blocktype=="movedown":
                    self.field.moveRobotDown()
                if self.data[x][y].blocktype=="moveleft":
                    self.field.moveRobotLeft()  
                if self.data[x][y].blocktype=="moveright":
                    self.field.moveRobotRight()

        def find(self,fieldtype):
             foundfields = []
             ftype = pointer.Pointer(0,0)
             ftype.found = False
             ftype.x = 0
             ftype.y = 0
             for y in xrange(self.size):
                 for x in xrange(self.size):
                     if self.data[x][y].blocktype == fieldtype:
                         ftype.found = True
                         ftype.x = x
                         ftype.y = y
                         foundfields.append(ftype)
             return foundfields

        def printPointer(self): 
            for p in self.pointers:
                print "p: x:" + str(p.x) + " y:" + str(p.y) 


        def doIteration(self):
            for s in self.find("spawn"):
                print "found spawn"
                self.pointers.append(pointer.Pointer(s.x,s.y))
              
            self.printPointer() 
            appendPointers = []
            removePointers = []
            for p in self.pointers:
                removePointers.append(p)
                if self.canPlacePointer(p.x,p.y-1):
                    appendPointers.append(pointer.Pointer(p.x,p.y-1))
                if self.canPlacePointer(p.x,p.y+1):
                    appendPointers.append(pointer.Pointer(p.x,p.y+1))
                if self.canPlacePointer(p.x-1,p.y):
                    appendPointers.append(pointer.Pointer(p.x-1,p.y))
                if self.canPlacePointer(p.x+1,p.y):
                    appendPointers.append(pointer.Pointer(p.x+1,p.y))
            for p in removePointers:
                self.pointers.remove(p)

            for p in appendPointers:
                self.pointers.append(p)

            for p in self.pointers:
                self.performAction(p.x,p.y)




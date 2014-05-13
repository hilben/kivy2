import pointer
import logicblock

class Logic:

    def __init__(self, size,field):
        self.size=size
        self.field = field
        self.data = []
        self.state = 0
        for y in xrange(size):
            self.data.append([])
            for x in xrange(size):
                self.data[y].append(logicblock.LogicBlock("","_"))

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
        row = 1
        for y in xrange(self.size):
            printStr += str(row)
            row += 1
            for x in xrange(self.size):
                printStr = str(printStr) + "\t" + str(self.data[x][y].blocktype)
                for p in self.getPointerAt(x,y):
                    printStr += "*"
            printStr += "\n"

        print printStr
        self.printPointer()

    def getBlock(self,x,y):
        if self.isOnField(x,y):
            return self.data[x][y]
        else:
            return logicblock.LogicBlock("","e")

    def canPlacePointer(self,x,y):
        #print "canplace: " + str(x) + " " + str(y)
        if len(self.getPointerAt(x,y))>3:
            print "cant place more pointers at " + str(x) + " " + str(y) + " exceeded max of 3"
            return False
        if self.isOnField(x,y):
            if self.data[x][y].blocktype == "e" or self.data[x][y].blocktype == "_":
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
                if self.data[x][y].blocktype[0] == "s":
                    return self.data[x][y].blocktype[1] == str(self.state)
                return True
        else:
            return False

    def countAction(self,curpointer):
        x = curpointer.x
        y = curpointer.y
        #TODO: just use an array here...
        if self.isOnField(x,y):
            if self.data[x][y].blocktype=="mu":
                self.incrDict("mu")
            if self.data[x][y].blocktype=="md":
                self.incrDict("md")
            if self.data[x][y].blocktype=="ml":
                self.incrDict("ml")
            if self.data[x][y].blocktype=="mr":
                self.incrDict("mr")
            if self.data[x][y].blocktype=="S+":
                self.incrDict("S+",3)
            if self.data[x][y].blocktype=="S-":
                self.incrDict("S-",3)
   
    

    def incrDict(self,action,value=1):
        if (self.actions.get(action)==None):
            self.actions[action]=value
        else:
            self.actions[action]=self.actions[action]+value

    def doMostUrgentAction(self):
        currentMax = -1
        duplicates = False
        maxAction = "none"
        for action, count in self.actions.iteritems():
            if count>currentMax:
                maxAction = action
                currentMax = count
                duplicates = False
            elif count==currentMax:
                duplicates = True

        if duplicates==True or currentMax<=0:
             maxAction = "none"
        if maxAction=="mu":
            self.field.moveRobotUp()
        if maxAction=="md":
            self.field.moveRobotDown()
        if maxAction=="ml":
            self.field.moveRobotLeft()
        if maxAction=="mr":
            self.field.moveRobotRight()
        if maxAction=="S+":
            self.incrState()
        if maxAction=="S-":
            self.decrState()
   
    def incrState(self):
        self.state = (self.state + 1) % 10
        self.pointers = []

    def decrState(self):
        self.state = (self.state - 1) % 10
        self.pointers = []

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
        print "LOGIC: reset logic..."
        self.pointers = []
        self.state = 0

    def start(self):
        self.reset()
        for s in self.find("s"):
            self.pointers.append(pointer.Pointer(s.x,s.y))

    #removes all pointers at a given position
    def removePointers(self,x,y,maxNumber=-1):
        removes = []
        currentNumber = maxNumber
        for p in self.pointers:
            if p.x == x and p.y == y:
                removes.append(p)
        for p in removes:
            if currentNumber != 0:
                currentNumber -= 1
                self.pointers.remove(p)

    def doIteration(self):
        appendPointers = []
        removePointers = []
        self.actions = {}

        print "pointer before append:"
        self.printPointer()
        
        print "current state:" + str(self.state)
        #Perform actions at place with active pointers
        for p in self.pointers:
            self.countAction(p)
        self.doMostUrgentAction()
        print self.actions

        #send pointers to neighbours
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
        #remove all pointers of previous iteration
        for p in removePointers:
            self.pointers.remove(p)
        #add the pointers which are added to neighbours
        for p in appendPointers:
            self.pointers.append(p)
        #spawn new pointers
        for s in self.find("a"):
            self.pointers.append(pointer.Pointer(s.x,s.y))
        
        #remove pointers of fields  with too many pointers
        for y in xrange(self.size):
            for x in xrange(self.size):
                if len(self.getPointerAt(x,y))>3:
                    print "removing pointers because too crowded at" + str(x) + " " + str(y)
                    self.removePointers(x,y,len(self.getPointerAt(x,y))-3)

        print "pointer after update"
        self.printPointer()

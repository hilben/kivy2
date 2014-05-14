import pointer

class Field:

    data=[]
    size=0
    collects=0

    def __init__(self, size):
        self.size=size
        for y in xrange(size):
            self.data.append([])
            for x in xrange(size):
                self.data[y].append('_')

    def isOnField(self,x,y):
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            return True
        else:
            return False

    def setRobot(self,x,y):
        if not self.isOnField(x,y):
            raise FieldException("Placing robot out of field")
        if self.data[x][y]=="#":
            self.collects += 1
        if not self.data[x][y]=="X":
            self.setBlock(x,y,"M")
        else:
            print "The robot died"
            if self.getNumberOfCollectables()==0:
                print "Everything collected level is done"

    def setBlock(self,x,y,block):
        if self.isOnField(x,y):
            self.data[x][y] = block

    def isFinished(self):
        return self.getNumberOfCollectables()==0

    def isCollectable(self,x,y):
        if self.isOnField(x,y):
            return self.data[x][y]=="#"
        return False

    def isPassableBlock(self,x,y):
        if self.isOnField(x,y):
            if self.data[x][y]!="+":
                return True
            return False
        return False

    def setCollectable(self,x,y):
        self.setBlock(x,y,"#")

    def setFree(self,x,y):
        self.setBlock(x,y,"_")

    def setWall(self,x,y):
        self.setBlock(x,y,"+")

    def setDead(self,x,y):
        self.setBlock(x,y,"X")

    def findRobot(self):
        robot = pointer.Pointer(0,0)
        robot.found = False
        robot.x = 0
        robot.y = 0
        for y in xrange(self.size):
            for x in xrange(self.size):
                if self.data[x][y] == "M":
                    robot.found = True
                    robot.x = x
                    robot.y = y
                    return robot
        raise FieldException("can not find robot. It might died")

    def moveRobotUp(self):
        robot = self.findRobot()
        if self.isPassableBlock(robot.x,robot.y-1):
            self.setFree(robot.x,robot.y)
            self.setRobot(robot.x,robot.y-1)
        else:
            print 'cant move there'

    def moveRobotDown(self):
        robot = self.findRobot()
        if self.isPassableBlock(robot.x,robot.y+1):
            self.setFree(robot.x,robot.y)
            self.setRobot(robot.x,robot.y+1)
        else:
            print 'cant move there'

    def moveRobotLeft(self):
        robot = self.findRobot()
        if self.isPassableBlock(robot.x-1,robot.y):
            self.setFree(robot.x,robot.y)
            self.setRobot(robot.x-1,robot.y)
        else:
            print 'cant move there'


    def moveRobotRight(self):
        robot = self.findRobot()
        if self.isPassableBlock(robot.x+1,robot.y):
            self.setFree(robot.x,robot.y)
            self.setRobot(robot.x+1,robot.y)
        else:
            print 'cant move there'

    def getNumberOfCollectables(self):
        return len(self.find("#"))


    def find(self,fieldtype):
        foundfields = []
        ftype = pointer.Pointer(0,0)
        ftype.x = 0
        ftype.y = 0
        for y in xrange(self.size):
            for x in xrange(self.size):
                if self.data[x][y] == fieldtype:
                    ftype.x = x
                    ftype.y = y
                    foundfields.append(ftype)
        return foundfields



    def printBlocks(self):
        print "printing blocks : " + str(self.size)
        printStr = ""
        for y in range(self.size):
            print printStr + "\n"
            printStr = str(y) + ": "
            for x in range(self.size):
                printStr = printStr +" " + self.data[x][y]
                print printStr
                self.printDebug()

    def getBlock(self,x,y):
        if self.isOnField(x,y):
            return self.data[x][y]
        else:
            return '+'

    def printDebug(self):
        print "\n","Collectables left: " + str(self.getNumberOfCollectables()), "Done " + str(self.getNumberOfCollectables()==0) ,  "Robot at x:" + str(self.findRobot().x) + " " + str(self.findRobot().y)

class FieldException(Exception):
    pass

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
                raise Exception("Placing robot out of field")
            if self.data[x][y]=="#":
                self.collects += 1
            self.setBlock(x,y,"M")

        def setBlock(self,x,y,block):
            if self.isOnField(x,y):
                self.data[x][y] = block

        def isCollectable(self,x,y):
            if self.isOnField(x,y):
                return self.data[x][y]=="#"
            return False

        def isPassableBlock(self,x,y):
            if self.isOnField(x,y):
                if self.data[x][y]=="#" or self.data[x][y]=="_":
                    return True
                return False
            return False

        def setCollectable(self,x,y):
            self.setBlock(x,y,"#")

        def setFree(self,x,y):
            self.setBlock(x,y,"_")

        def setWall(self,x,y):
            self.setBlock(x,y,"+")

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
             raise Exception("can not find robot")

        def moveRobotUp(self):
             robot = self.findRobot()
             print 'Trying to move robot to ' + str( robot.x) + " "  + str( robot.y-1)
             if self.isPassableBlock(robot.x,robot.y-1):
                 self.setFree(robot.x,robot.y)
                 self.setRobot(robot.x,robot.y-1)	
             else:
                 print 'cant move there'

        def moveRobotDown(self):
             robot = self.findRobot()
             print 'Trying to move robot to ' + str(robot.x) + " " + str(robot.y+1)
             if self.isPassableBlock(robot.x,robot.y+1):
                 self.setFree(robot.x,robot.y)
                 self.setRobot(robot.x,robot.y+1)	
             else:
                 print 'cant move there'

        def moveRobotLeft(self):
             robot = self.findRobot()
             print 'Trying to move robot to ' + str( robot.x-1) + " " + str( robot.y)
             if self.isPassableBlock(robot.x-1,robot.y):
                 self.setFree(robot.x,robot.y)
                 self.setRobot(robot.x-1,robot.y)	
             else:
                 print 'cant move there'


        def moveRobotRight(self):
             robot = self.findRobot()
             print 'Trying to move robot to ' + str( robot.x+1) + " " + str( robot.y)
             if self.isPassableBlock(robot.x+1,robot.y):
                 self.setFree(robot.x,robot.y)
                 self.setRobot(robot.x+1,robot.y)	
             else:
                 print 'cant move there'


 
        def printBlocks(self):
             printStr = ""
             for y in xrange(self.size):
                 print printStr + "\n"
                 printStr = ""
                 for x in xrange(self.size):
                     printStr = printStr + self.data[x][y] 

        def getBlock(self,x,y):
            if self.isOnField(x,y):
                return self.data[x][y]
            else:
                return '+'

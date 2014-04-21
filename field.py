class Field:
	
	data=[]
	size=0

	def __init__(self, size):
	    self.size=size
            for y in xrange(size):
                self.data.append([])
                for x in xrange(size):
		    self.data[y].append('+')
        
	def isOnField(self,x,y):
            if x >= 0 and x < self.size and y >= 0 and y < self.size:
                return True
	    else:
		return False
	
	def setRobot(self,x,y):
            self.setBlock(x,y,"M")

	def setBlock(self,x,y,block):
	    if self.isOnField(x,y):
                self.data[x][y] = block

	def setCollectable(self,x,y):
	    self.setBlock(x,y,"#")

        def setFree(self,x,y):
	    self.setBlock(x,y,"_")

	def setWall(self,x,y):
            self.setBlock(x,y,"+")

        #TODO: assuming just one robot exists
	def moveRobotUp(self):
	     robot = Field(0) 
	     robot.found = False
	     robot.x = 0
	     robot.y = 0
             for y in xrange(self.size):
                for x in xrange(self.size):
			if self.data[x][y] == "M":
			    self.setFree(x,y)
		            self.setRobot(x,y-1)
			    robot.found = True
			    robot.x = x
			    robot.y = y 
			    break

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

import field

class KivyRunner:


    currentLevel = 0
    level = field.Field(1)


    def __init__(self):
	    self.level = field.Field(10)


    def loadLevel(self,number):
        self.level = field.Field(10)

	if number==0:
	    self.level.setRobot(4,4)


    def nextLevel(self):
	    self.currentLevel = self.currentLevel + 1
	    self.loadLevel(self.currentLevel)

    def previousLevel(self):
	    if self.currentLevel > 0:
	        self.currentLevel = self.currentLevel - 1
                self.loadLevel(self.currentLevel)


    def reset(self):
	    self.loadLevel(self.currentLevel)

    def setLogic(self,logic):
	   self.reset()
	   self.logic = logic


    def getPointer(self):
	   return self.logic.pointers

    def getFieldData(self):
           return self.level.data


    def doIteration(self):
	    self.logic.doIteration()
	    self.level.printBlocks()
	    self.logic.printBlocks()




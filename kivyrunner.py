import field

class KivyRunner:


    currentLevel = 0
    level = field.Field(1)

    def __init__(self):
	    level = field.Field(10)


    def loadLevel(self,number):
            print 'not implemented'


    def nextLevel(self):
	    currentLevel = currentLevel + 1
	    self.loadLevel(currentLevel)

    def previousLevel(self):
	    if currentLevel > 0:
	        currentLevel = currentLevel - 1
	        self.loadLevel(currentLevel)

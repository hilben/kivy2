import field
import logic
import logicblock 

class KivyRunner:

    currentLevel = 0
    level = field.Field(1)

    def __init__(self):
        self.level = field.Field(10)


    def loadLevel(self,number):
        self.level = field.Field(10)
        self.currentLevel = number
        f = open("level"+str(number),"r")
        level = field.Field(10)
        x,y = 0,0
        for line in f:
            x = 0
        for s in line:
            if (s!="\n"):
                self.level.setBlock(x,y,s)
            x += 1
            y +=1

    #debug method to load logic out of file
    def loadLogic(self,filename):

        f = open(filename,"r").read()
        self.logic = logic.Logic(6,self.level)
        x,y = 0,0
        lines = f.split("\n")
        for line in lines:
            x = 0
            entries = line.split(" ")
            for s in entries:
                self.logic.setBlock(x,y,logicblock.LogicBlock("",s))
                #print "x " + str(x) + " y " + str(y) + " s:" +  str(s)
                x += 1
            y += 1

    def nextLevel(self):
        self.currentLevel = self.currentLevel + 1
        self.loadLevel(self.currentLevel)

    def previousLevel(self):
        if self.currentLevel > 0:
            self.currentLevel = self.currentLevel - 1
            self.loadLevel(self.currentLevel)


    def reset(self):
        self.loadLevel(self.currentLevel)
        self.logic.reset()
        self.logic.start() #TODO: put into separate function

    def setLogic(self,logic):
        self.reset()
        self.logic = logic


    def getPointer(self):
        return self.logic.pointers

    def getFieldData(self):
        return self.level.data


    def doIteration(self):
        try:
            self.logic.doIteration()
            self.logic.printBlocks()
            self.level.printBlocks()
        except field.FieldException as e:
            print "Level was reseted`because: "
            print str(e)
        self.reset()

    def isLevelFinished(self):
        return self.field.getNumberOfCollectables()<1

    def getLogicBoxes(self):
        logicBoxes = []
        logicBoxes.append(logicblock.LogicBlock("image1","_"))
        logicBoxes.append(logicblock.LogicBlock("image2","+"))
        logicBoxes.append(logicblock.LogicBlock("image3","#"))
        logicBoxes.append(logicblock.LogicBlock("image4","a"))
        logicBoxes.append(logicblock.LogicBlock("image5","s"))
        logicBoxes.append(logicblock.LogicBlock("image5","_"))
        logicBoxes.append(logicblock.LogicBlock("image6","_"))
        logicBoxes.append(logicblock.LogicBlock("image7","_"))
        logicBoxes.append(logicblock.LogicBlock("image8","_"))
        logicBoxes.append(logicblock.LogicBlock("image9","_"))
        logicBoxes.append(logicblock.LogicBlock("image10","_"))
        return logicBoxes


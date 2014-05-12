import field
import logic
import logicblock 

class KivyRunner:

    currentLevel = 0
    level = field.Field(1)

    def __init__(self):
        self.level = field.Field(10)
 	self.logic = logic.Logic(6,self.level) 	

    def loadLevel(self,number):
        self.level = field.Field(10)
        self.currentLevel = number
        levelname = "levels/level"+str(number)
        print "loading level: " + levelname
        f = open(levelname,"r")
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
        return self.level.getNumberOfCollectables()<1

    def getLogicBoxes(self):
        logicBoxes = []
        logicBoxes.append(logicblock.LogicBlock("block_blank","_"))
        logicBoxes.append(logicblock.LogicBlock("logic_wu.png","wu"))
        logicBoxes.append(logicblock.LogicBlock("logic_wd.png","wd"))
        logicBoxes.append(logicblock.LogicBlock("logic_wl.png","wl"))
        logicBoxes.append(logicblock.LogicBlock("logic_wr.png","wr"))

        logicBoxes.append(logicblock.LogicBlock("logic_cu.png","cu"))
        logicBoxes.append(logicblock.LogicBlock("logic_cd.png","cd"))
        logicBoxes.append(logicblock.LogicBlock("logic_cl.png","cl"))
        logicBoxes.append(logicblock.LogicBlock("logic_cr.png","cr"))

        logicBoxes.append(logicblock.LogicBlock("logic_spawn.png","s"))
        logicBoxes.append(logicblock.LogicBlock("logic_aspawn.png","a"))
        logicBoxes.append(logicblock.LogicBlock("logic_state_up.png","s+"))
        logicBoxes.append(logicblock.LogicBlock("logic_state_down.png","s-"))

        logicBoxes.append(logicblock.LogicBlock("logic_s0.png","s0"))
        logicBoxes.append(logicblock.LogicBlock("logic_s1.png","s1"))
        logicBoxes.append(logicblock.LogicBlock("logic_s2.png","s2"))
        logicBoxes.append(logicblock.LogicBlock("logic_s3.png","s3"))
        logicBoxes.append(logicblock.LogicBlock("logic_s4.png","s4"))
        logicBoxes.append(logicblock.LogicBlock("logic_s5.png","s5"))
        logicBoxes.append(logicblock.LogicBlock("logic_s6.png","s6"))
        logicBoxes.append(logicblock.LogicBlock("logic_s7.png","s7"))
        logicBoxes.append(logicblock.LogicBlock("logic_s8.png","s8"))
        logicBoxes.append(logicblock.LogicBlock("logic_s9.png","s9"))

        logicBoxes.append(logicblock.LogicBlock("logic_mu.png","mu"))
        logicBoxes.append(logicblock.LogicBlock("logic_md.png","md"))
        logicBoxes.append(logicblock.LogicBlock("logic_ml.png","ml"))
        logicBoxes.append(logicblock.LogicBlock("logic_mr.png","mr"))
        return logicBoxes


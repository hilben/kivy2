import pointer
import field 
import kivyrunner
import logic 
import logicblock

game = kivyrunner.KivyRunner()

logicfield = logic.Logic(6,game.level)
#logicfield.setBlock(0,0,logicblock.LogicBlock("","s"))
#logicfield.setBlock(1,0,logicblock.LogicBlock("","wd"))
#logicfield.setBlock(2,0,logicblock.LogicBlock("","ml"))
#logicfield.setBlock(0,2,logicblock.LogicBlock("","s"))
#logicfield.setBlock(1,2,logicblock.LogicBlock("","wl"))
#logicfield.setBlock(2,2,logicblock.LogicBlock("","mu"))

#logicfield.setBlock(0,4,logicblock.LogicBlock("","s"))
#logicfield.setBlock(1,4,logicblock.LogicBlock("","wu"))
#logicfield.setBlock(2,4,logicblock.LogicBlock("","mr"))
#
#logicfield.setBlock(4,0,logicblock.LogicBlock("","s"))
#logicfield.setBlock(4,1,logicblock.LogicBlock("","wr"))
#logicfield.setBlock(4,2,logicblock.LogicBlock("","md"))

game.loadLevel(2)
#game.setLogic(logicfield)
game.loadLogic("logic1")

while raw_input("enter any key"):    
    game.doIteration()

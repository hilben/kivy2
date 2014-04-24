import pointer
import field 
import kivyrunner
import logic 
import logicblock

print 'hello world'

	
def performActionOnField(action, field):
    print "to be implemneted"





size = 10

pointers = []
pointers.append(pointer.Pointer(3,10))


print "trying to create field:"

game = kivyrunner.KivyRunner()

logicfield = logic.Logic(6,game.level)
logicfield.setBlock(0,0,logicblock.LogicBlock("","spawn"))
logicfield.setBlock(1,0,logicblock.LogicBlock("","movedown"))
logicfield.setBlock(2,0,logicblock.LogicBlock("","moveright"))
logicfield.printBlocks()

game.loadLevel(0)
game.setLogic(logicfield)

for x in range(0,4):
    game.doIteration()

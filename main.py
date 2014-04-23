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
robotfield = field.Field(10)
robotfield.setRobot(3,3)
robotfield.setCollectable(3,4)
robotfield.setCollectable(2,4)
robotfield.setCollectable(1,4)
robotfield.setCollectable(3,5)
robotfield.setCollectable(3,6)
robotfield.setCollectable(3,7)
robotfield.setFree(4,4)
robotfield.setFree(4,5)
robotfield.setFree(4,6)
robotfield.setFree(5,4)


logicfield = logic.Logic(6,robotfield)
logicfield.setBlock(0,0,logicblock.LogicBlock("","spawn"))
logicfield.setBlock(1,0,logicblock.LogicBlock("","movedown"))
logicfield.setBlock(2,0,logicblock.LogicBlock("","moveright"))
logicfield.printBlocks()


robotfield.printBlocks()
robotfield.moveRobotLeft()
robotfield.moveRobotDown()
robotfield.moveRobotDown()
robotfield.moveRobotLeft()


robotfield.moveRobotUp()
robotfield.printBlocks()


logicfield.doIteration()
robotfield.printBlocks()
logicfield.doIteration()
robotfield.printBlocks()
logicfield.printBlocks()

logicfield.doIteration()
robotfield.printBlocks()
logicfield.printBlocks()
#logic:
# check if there are pointers else:
# For all field on the logicboard
# create a pointer on each input field
# 

# for all pointers
# delete this pointer and
# for all neighbors of this pointer
# if the neighbar was already reached --> discard
# if the neighbour is outut field --> trigger and delete pointera
# if the neighbour is a condition create a pointer on the condition field if the condition holds
#

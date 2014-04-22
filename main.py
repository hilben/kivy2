import pointer
import field 
import kivyrunner

print 'hello world'

def continueCodingBlocks(pointers, blocks, field):
	if len(pointers)>0:
	    for p in pointers:
                print blocks.getBlock(p.x,p.y) 
	
	
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


logicfield = field.Field(10)
continueCodingBlocks(pointers, logicfield, robotfield)

robotfield.printBlocks()
robotfield.moveRobotUp()
robotfield.printBlocks()

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

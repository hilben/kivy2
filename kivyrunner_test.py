import kivyrunner
import unittest
import field
class KivyRunnerTest(unittest.TestCase):


    field
    def test_field(self):
            self.field = field.Field(10)

	    self.assertNotEqual(self.field.isOnField(-1,0),True)
	    self.assertNotEqual(self.field.isOnField(0,-1),True)
	    self.assertNotEqual(self.field.isOnField(10,0),True)
	    self.assertNotEqual(self.field.isOnField(1,10),True)
            self.assertEqual(self.field.isOnField(3,3),True)

	    with self.assertRaises(Exception):
                self.field.setRobot(-1,-1)
	    with self.assertRaises(Exception):
                self.field.findRobot()
	    self.field.setRobot(5,5)
            self.assertEqual(self.field.isPassableBlock(5,4),True)            
	    self.field.setWall(5,4)
	    self.assertEqual(self.field.isPassableBlock(5,4),False)
            
            self.assertTrue(self.robot_at(5,5))

	    self.field.moveRobotUp()
	    self.assertTrue(self.robot_at(5,5))

	    self.field.moveRobotDown()
	    self.field.moveRobotDown()
	    self.assertTrue(self.robot_at(5,7)) 

            self.field.moveRobotDown()
            self.field.moveRobotDown()
            self.field.moveRobotDown()
            self.field.moveRobotDown()
	    self.assertTrue(self.robot_at(5,9))

            #Place 4 collectables which they robot should collect
            self.field.setCollectable(0,5)
	    self.field.setCollectable(4,0)
	    self.field.setCollectable(4,9)
	    self.field.setCollectable(9,5)
	    self.assertTrue(self.field.isCollectable(4,9))
	    self.assertTrue(self.field.isCollectable(9,5))
	    self.assertTrue(self.field.isCollectable(0,5))
	    self.assertTrue(self.field.isCollectable(4,0))
            self.assertEqual(self.field.getNumberOfCollectables(),4)
             
            #Testing for not breaking the borders
	    for x in range(1,20):
		    self.field.moveRobotLeft()
            self.assertTrue(self.robot_at(0,9))
            self.assertEqual(self.field.getNumberOfCollectables(),3)
	    for x in range(1,20):
		    self.field.moveRobotUp()
            self.assertTrue(self.robot_at(0,0))
            self.assertEqual(self.field.getNumberOfCollectables(),2)
            for x in range(1,20):
		    self.field.moveRobotRight()
            self.assertTrue(self.robot_at(9,0))
            self.assertEqual(self.field.getNumberOfCollectables(),1)
            for x in range(1,20):
		    self.field.moveRobotDown()
            self.assertTrue(self.robot_at(9,9))
            self.assertEqual(self.field.getNumberOfCollectables(),0)
            self.assertEqual(self.field.collects,4)
            self.assertTrue(self.field.finished)


    def robot_at(self,x,y):
	    r = self.field.findRobot()
	    print "robot at " + str(x) + " " + str(y)
            return r.x==x and r.y==y and r.found==True


    def test_something(self):
	    self.assertEqual(5,5)

    def test_something2(self):
	    self.assertNotEqual(5,6)


unittest.main()    

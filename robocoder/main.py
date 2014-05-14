import pointer
import field
import kivyrunner
import logic
import logicblock



#
# This class is used to test the roborunner indepentently from kivy
#
#

game = kivyrunner.KivyRunner(10)
game.loadLevel(1)
game.loadLogic("levels/logic2")
game.reset()

run = True
while run:
    a=raw_input("enter")
    if a=="r":
        game.loadLogic("levels/logic2")
    if a=="q":
        run = False
    game.doIteration()

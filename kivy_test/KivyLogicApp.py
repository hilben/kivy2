from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from robocoder.kivyrunner import KivyRunner

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):  
        super(MainLayout, self).__init__(**kwargs)
        #self.kivyrunner = KivyRunner()

class GameLogic(FloatLayout):
    def __init__(self, **kwargs):  
        super(GameLogic, self).__init__(**kwargs)

class LogicBlocksGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LogicBlocksGridLayout, self).__init__(**kwargs)
        #print  "AAAAAAAAAAAAAAAAAAAAAA" + str(self.ids)
        self.kivyrunner = KivyRunner()
        logic_boxes = self.kivyrunner.getLogicBoxes()

        #TODO: use OS.Lineseperator
        for logic_box in logic_boxes:
            wimg = Image(source="images/"+logic_box.picture)
            self.add_widget(wimg)


class PlayingField(GridLayout):
    def __init__(self, **kwargs):  
        super(PlayingField, self).__init__(**kwargs)
        self.kivyrunner = KivyRunner()
        self.kivyrunner.loadLevel(1)

        level = self.kivyrunner.level

        for x in xrange(level.size):
            for y in xrange(level.size):
                if level.data[x][y]=="#":
                    wimg = Image(source="images/block_collectable.png")
                elif level.data[x][y]=="X":
                    wimg = Image(source="images/block_death.png")
                elif level.data[x][y]=="_":
                    wimg = Image(source="images/block_blank.png")
                elif level.data[x][y]=="M":
                    wimg = Image(source="images/block_robot.png")
                else:
                    wimg = Image(source="images/block_wall.png")
                self.add_widget(wimg)


class KivyLogicApp(App):

    def build(self):
        return MainLayout()

if __name__ == "__main__":
    KivyLogicApp().run()

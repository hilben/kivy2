from kivy.app import App
#from kivy.garden.magnet import Magnet
from magnet import Magnet

from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

from os import listdir

from kivy.graphics import Color, Line, Rectangle



class LogicElement(Label):
    pass

class MyScatter(Scatter):
    pass

class GameLogic(BoxLayout):
    def copy_logic_element(self):

        a = MyScatter()
        b = LogicElement(text='Blubber')
        a.add_widget(b)
        self.add_widget(a)

class GridLayoutWithGrid(GridLayout):
    def create_grid_points(self):
        r = self.rows
        c = self.cols

        x, y = self.pos
        h, b = self.size

class GridTest(GridLayout):
    def autofill(self, k):
        self.cols = k
        for i in range(k):
            self.add_widget(Button(text=str(i)))

 
class KivyRunnerApp(App):
    def build(self):
        pass
 
if __name__ == '__main__':
    KivyRunnerApp().run()
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
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import NumericProperty, ListProperty, DictProperty

from os import listdir

from kivy.graphics import Color, Line, Rectangle

from kivyrunner import KivyRunner

from kivy.logger import Logger

import random


class LogicElement(Label):
    pass

class MyScatter(Scatter):
    pass

class GameLogic(FloatLayout):

    def __init__(self, **kwargs):  
        super(GameLogic, self).__init__(**kwargs)
        self.kivyrunner = KivyRunner()
        logic_boxes = self.kivyrunner.getLogicBoxes()

        #self.abc.text = 'Asdfasdf'
        self.ids.logic_blocks_grid.add_widget(Label(text = 'Asdfasdfasdfasdfasdfdefaasfdasdf'))
        #print('###########################'+str(self.ids))
        #self.ids.abc.text = 'Asdf'
        #grid = self.ids['logic_blocks_grid']
        #grid.add_widget(Label(text = 'Asdfasdf'))
        #for logic_box in logic_boxes:
        #    self.ids.logic_blocks_grid.add_widget(Label(text = logic_box.picture))

        #self.add_widget(Label(text = str(self.blubber5)))
        #self.add_widget(Label(text = 'Ssdfsdfsdf'))

    def test():
        self.ids.abc.text = 'Asdf'

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


class OurScreenManager(ScreenManager):
    def __init__(self, **kwargs):  
        super(OurScreenManager, self).__init__(**kwargs)

class ScatterTextWidget(BoxLayout):
    def __init__(self, **kwargs):  
        super(ScatterTextWidget, self).__init__(**kwargs)
        #print('++++++++++++++'+str(self.ids))

    def change_label_colour(self, *args):
        colour = [random.random() for i in xrange(3)] + [1]
        label = self.ids['my_label']

        self.ids.my_label_2.color = colour

        label.color = colour
        Logger.info('++++++++++++++'+str(self.ids))
        #print('++++++++++++++'+str(self.ids))


class KivyRunnerApp(App):
    def build(self):
        scr = OurScreenManager()
        #print('++++++++++++++'+str(scr.ids))
        return scr
 
if __name__ == '__main__':
    KivyRunnerApp().run()
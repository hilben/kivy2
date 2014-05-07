import sys
sys.path.append('robocoder')

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

from kivyrunner import KivyRunner


kv = '''
MainLayout:
    GameLogic:
        BoxLayout:
            orientation: 'vertical'
            LogicBlocksGridLayout:
            #GridLayout:
            #    id: logic_blocks_grid
            #    cols: 6
            GridLayout:
                id: logic_field_grid
                cols: 6
                rows: 6
    PlayingField:

<LogicBlocksGridLayout>:
    cols: 6



<PlayingField>:
    cols: 10
    rows: 10

'''

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

		for logic_box in logic_boxes:
			pass
			self.add_widget(Label(text= logic_box.picture))


class PlayingField(GridLayout):
	def __init__(self, **kwargs):  
		super(PlayingField, self).__init__(**kwargs)
		self.kivyrunner = KivyRunner()
		self.kivyrunner.loadLevel(1)

		level = self.kivyrunner.level

		for x in xrange(level.size):
			for y in xrange(level.size):
			    self.add_widget(Label(text= level.data[x][y]))

class KivyLogic2App(App):
    def build(self):
        self.root = Builder.load_string(kv)

        return self.root

if __name__ == "__main__":
	KivyLogic2App().run()
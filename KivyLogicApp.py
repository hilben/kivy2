from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivyrunner import KivyRunner

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


class KivyLogicApp(App):

    def build(self):
    	return MainLayout()

if __name__ == "__main__":
    KivyLogicApp().run()
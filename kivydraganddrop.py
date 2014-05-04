from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.clock import Clock
from kivy.properties import ListProperty, ObjectProperty

from kivy.lang import Builder

from magnet import Magnet
from kivy.uix.image import Image

from kivyrunner import KivyRunner

from os import listdir

IMAGEDIR = 'kivy/pics/'

IMAGES = filter(
    lambda x: x.endswith('.png'),
    listdir(IMAGEDIR))

kv = '''
<DaDLayout>:
	b: app.a
	BoxLayout:
		orientation: 'vertical'
		GridLayout:
			
			id: grid_1
			cols: 10
			rows: 3

		GridLayout:
			id: grid_2
			cols: 10

<MyLabel>:
    canvas.before:
        Color:
            rgb: (255, 0, 0)
        Rectangle:	
        	pos: self.pos
            size: self.size
	text: self.c.text

	Image:
		source: str(root.c.pic)
		pos: root.pos

	#on_touch_down: root.create_copy()

'''
class Thing(object):
	def __init__(self, text, pic):
		self.text = text
		self.pic = pic

	def get_text(self):
		return self.text

class MyLabel(Label):
	c = ObjectProperty()



class DaDLayout(FloatLayout):
	#b = ListProperty()

	def __init__(self, **kwargs):  
		super(DaDLayout, self).__init__(**kwargs)
		Clock.schedule_once(self.populate_grid_1)

	def populate_grid_1(self, abc):

		#print('####################123')

		self.ids.grid_1.add_widget(Button(text='123'))

		#print('***************'+str(self.b))

		for c in self.b:
		#	#print('++++++++++++++'+str(c))
			l = MyLabel(c = c)
			self.ids.grid_1.add_widget(l)

	def create_copy(self):
		print('*++++++++++++++++++++++++++')



class DaDApp(App):
	#a = ListProperty(None)
    a = ListProperty()

    def build(self):
		

		for i in IMAGES:
			#image = Image(source=IMAGEDIR + i, size=(32, 32), size_hint=(None, None))
			self.a.append(Thing(str(i+str(66)), IMAGEDIR + i))
			
		Builder.load_string(kv)
		#self.root = Builder.load_string(kv)

		return DaDLayout()

if __name__ == "__main__":
	DaDApp().run()
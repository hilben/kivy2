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

	#Image:
	#	source: str(root.c.pic)
	#	pos: root.pos

	#on_touch_down: root.create_copy()

'''
class Thing(object):
	def __init__(self, text, pic, image):
		self.text = text
		self.pic = pic
		self.image = image

	def get_text(self):
		return self.text

class MyLabel(Label):
	c = ObjectProperty()
	app = ObjectProperty(None)
	img = ObjectProperty(None, allownone=True)

	def on_img(self, *args):
		self.clear_widgets()

		if self.img:
			Clock.schedule_once(lambda *x: self.add_widget(self.img), 0)

	def on_touch_down(self, touch, *args):
		if self.collide_point(*touch.pos):
			touch.grab(self)
			self.remove_widget(self)
			self.app.add_widget(self)
			self.center = touch.pos
			#self.img.center = touch.pos
			return True

		return super(MyLabel, self).on_touch_down(touch, *args)

    # def on_touch_move(self, touch, *args):
    #     grid_layout = self.app.root.ids.grid_layout
    #     float_layout = self.app.root.ids.float_layout

    #     if touch.grab_current == self:
    #         self.img.center = touch.pos
    #         if grid_layout.collide_point(*touch.pos):
    #             grid_layout.remove_widget(self)
    #             float_layout.remove_widget(self)

    #             for i, c in enumerate(grid_layout.children):
    #                 if c.collide_point(*touch.pos):
    #                     grid_layout.add_widget(self, i - 1)
    #                     break
    #             else:
    #                 grid_layout.add_widget(self)
    #         else:
    #             if self.parent == grid_layout:
    #                 grid_layout.remove_widget(self)
    #                 float_layout.add_widget(self)

    #             self.center = touch.pos

    #     return super(DraggableImage, self).on_touch_move(touch, *args)

    # def on_touch_up(self, touch, *args):
    #     if touch.grab_current == self:
    #         self.app.root.remove_widget(self.img)
    #         self.add_widget(self.img)
    #         touch.ungrab(self)
    #         return True

    #     return super(DraggableImage, self).on_touch_up(touch, *args)


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
			l = MyLabel(c = c, app = self, img = c.image)
			self.ids.grid_1.add_widget(l)

	def create_copy(self):
		print('*++++++++++++++++++++++++++')



class DaDApp(App):
	#a = ListProperty(None)
    a = ListProperty()

    def build(self):
		

		for i in IMAGES:
			image = Image(source=IMAGEDIR + i, size=(32, 32), size_hint=(None, None))
			self.a.append(Thing(str(i+str(66)), image))
			
		Builder.load_string(kv)
		#self.root = Builder.load_string(kv)

		return DaDLayout()

if __name__ == "__main__":
	DaDApp().run()
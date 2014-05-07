import sys
sys.path.append('kivy_lib')
sys.path.append('robocoder')


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

from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter

#from kivyrunner import Scatter


IMAGEDIR = 'images/'

IMAGES = filter(
    lambda x: x.endswith('.png'),
    listdir(IMAGEDIR))

kv = '''
ScreenManager:
    StartScreen:
    GameScreen:

<StartScreen@Screen>:
    name: 'menu'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'horizontal'
            #Renderer:
        BoxLayout:
            size_hint_y: 0.15
            orientation:'horizontal'
            Button:
                text: 'Start Game'
                on_press: root.manager.current = 'game'
            Button:
                text: 'End Game'
                on_press: app.stop()

<GameScreen@Screen>
    name: 'game'
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            orientation:'vertical'
            Button:
                size_hint_y: 0.15
                text: 'Go to Menu'
                on_press: root.manager.current = 'menu'
            BoxLayout:
                size_hint_y: 0.15
                orientation: 'horizontal'
                Label:
                    text: 'Level'
                Label:
                    text: '1, but make ma change!'
            DnDLayout:
            BoxLayout:
                size_hint_y: 0.15
                orientation: 'horizontal'
                Button:
                    text: 'Start'
                Button:
                    text: 'Reset Logic'
        FloatLayout:
            size_hint_x: 0.05
        GameGrid:
            Label:


<GameGrid>:
    canvas.before:
        Color:
            rgb: (0, 0, 50)
        Rectangle:  
            pos: self.pos
            size: self.size
    cols: 10
    rows: 10
    padding: 2
    spacing: 2

<DnDLayout>:
    list_of_img_dirs: app.list_of_img_dirs
    BoxLayout:
        orientation: 'vertical'
        GridLayout:
            canvas.before:
                Color:
                    rgb: (0, 0, 0)
                Rectangle:  
                    pos: self.pos
                    size: self.size
            id: grid_1
            cols: 6
            rows: 3
            padding: 2
            spacing: 2

        FloatLayout:
            size_hint_y: 0.05

        GridLayout:
            canvas.before:
                Color:
                    rgb: (0, 0, 0)
                Rectangle:  
                    pos: self.pos
                    size: self.size
            id: grid_2
            cols: 6
            rows: 6
            padding: 2
            spacing: 2

<BlackBoxLayout>:
    #size:(32, 32)
    canvas.before:
        Color:
            rgb: (90, 90, 90)
        Rectangle:  
            pos: self.pos
            size: self.size

<Grid>:

<MyLabel>:
    canvas.before:
        Color:
            rgb: (255, 0, 0)
        Rectangle:  
            pos: self.pos
            size: self.size
    text: self.c.text

    #Image:
    #   source: str(root.c.pic)
    #   pos: root.pos

    #on_touch_down: root.create_copy()

'''

class GameGrid(GridLayout):
    def __init__(self, **kwargs):  
        super(GameGrid, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_grid)

    def populate_grid(self, abc):
        n = self.cols*self.rows-5

        for i in range(n):
            b = BlackBoxLayout()
            #b.add_widget(Label(text='1'))
            self.add_widget(b)


class BlackBoxLayout(BoxLayout):
    pass

class Item(Image):
    dnd_layout = ObjectProperty(None)

    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos): #if it is touched on
            touch.grab(self)
            #self.remove_widget(self)
            self.scatter = Scatter(center = touch.pos, size= self.size, size_hint=(None, None))
            self.scatter.add_widget(Image(source = self.source))
            self.dnd_layout.add_widget(self.scatter)
            #self.center = touch.pos
            #self.img.center = touch.pos
            return True

        return super(Item, self).on_touch_down(touch, *args)

    def on_touch_move(self, touch, *args):
        grid_1 = self.dnd_layout.ids.grid_1
        grid_2 = self.dnd_layout.ids.grid_2

        if touch.grab_current == self:
            self.scatter.center = touch.pos
    
    def on_touch_up(self, touch, *args):
        grid_1 = self.dnd_layout.ids.grid_1
        grid_2 = self.dnd_layout.ids.grid_2
        
        check = False

        if touch.grab_current == self:
            for black_box in grid_2.children:
                #print(black_box)
                if black_box.collide_point(*touch.pos):
                    #if black_box.children
                    black_box.add_widget(Image(source = self.source))
                    self.dnd_layout.remove_widget(self.scatter)
                    check = True
            if not grid_2.collide_point(*touch.pos) or check==False:
                self.dnd_layout.remove_widget(self.scatter)

    #         self.app.root.remove_widget(self.img)
    #         self.add_widget(self.img)
    #         touch.ungrab(self)
    #         return True

    #     return super(DraggableImage, self).on_touch_up(touch, *args)

class DnDLayout(FloatLayout):

    def __init__(self, **kwargs):  
        super(DnDLayout, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_grids)

    def populate_grids(self, abc):
        grid_1 = self.ids.grid_1
        grid_2 = self.ids.grid_2

        for img_dir in self.list_of_img_dirs:
            #item = Item(source=img_dir, size=(32, 32), size_hint=(None, None), dnd_layout = self)
            item = Item(source=img_dir, dnd_layout = self)
            b = BlackBoxLayout()
            b.add_widget(item)
            grid_1.add_widget(b)
            #grid_1.add_widget(Label(text=str(k)))

        n = grid_2.cols*grid_2.rows

        for i in range(n):
            b = BlackBoxLayout()
            #b.add_widget(Label(text='1'))
            grid_2.add_widget(b)

class DnDApp(App):
    list_of_img_dirs = ListProperty()

    def build(self):
        c = Builder.load_string(kv)

        for i in IMAGES:
            self.list_of_img_dirs.append(IMAGEDIR + i)
            
        return c

if __name__ == "__main__":
    DnDApp().run()
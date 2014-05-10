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
from kivy.properties import ListProperty, ObjectProperty, StringProperty

from kivy.lang import Builder

from magnet import Magnet
from kivy.uix.image import Image

from kivyrunner import KivyRunner

from os import listdir

from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter

from kivy.uix.screenmanager import ScreenManager, Screen

#from kivyrunner import Scatter

from logicblock import LogicBlock



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

<GameScreen>
    kivyrunner: app.kivyrunner
    name: 'game'
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            size_hint_x: 0.35
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
                    #text: root.kivyrunner.currentLevel
            DnDLayout:
                id: dnd
            #    pos: root.pos
            #    size: root.size
            BoxLayout:
                size_hint_y: 0.15
                orientation: 'horizontal'
                Button:
                    text: 'Start'
                    on_press: root.start_game()
                Button:
                    text: 'Reset Logic'
                    on_press: dnd.reset_logic()
        FloatLayout:
            size_hint_x: 0.01
            #size_x: 5
        GameField:
            id: game_field
            size_hint_x: 0.6

<GameField>:
    kivyrunner: app.kivyrunner
    canvas.before:
        Color:
            rgb: (50, 50, 50)
        Rectangle:  
            pos: self.pos
            size: self.size
    cols: 10
    rows: 10
    padding: 2
    spacing: 2

<DnDLayout>:
    kivyrunner: app.kivyrunner
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
            canvas.before:
                Color:
                    rgb: (0, 0, 0)
                Rectangle:  
                    pos: self.pos
                    size: self.size
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
            rgb: (200, 200, 200)
        Rectangle:  
            pos: self.pos
            size: self.size

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

#<Blocks>:
    #size: (40, 40)
    #size_hint: (None, None)

<Item>:
    #size: (40, 40)
    #size_hint: (None, None)
'''
class GameScreen(Screen):
    def start_game(self):
        logic_grid = self.ids.dnd.ids.grid_2
        
        logic = [obj() for obj in [list]*6]

        r = 0
        c = 0

        for child in logic_grid.children:
            

                if not child.children:
                    #print('oooooooooooooooooooooooo'+'- empty')
                    picture = 'block_blank.png'
                    blocktype = '_'
                    logic_block = LogicBlock(picture, blocktype)
                else:
                     #print('oooooooooooooooooooooooo'+str(child.children[0]))
                    picture = child.children[0].picture
                    blocktype = child.children[0].blocktype
                    logic_block = LogicBlock(picture, blocktype)

                logic[r].append(logic_block)

                if c <= 5:
                    c += 1

                else:
                    c = 0
                    r += 1

        print('xxxxxxxxxxxxxxxxxx'+str(logic))
        

        ##### BAUSTELLE!!!!!!!!!!!####################################################################################

        self.kivyrunner.setLogic(logic)
        

        #update level
        game_field = self.ids.game_field

        level = self.kivyrunner.level
        level.data = self.kivyrunner.getFieldData()

        game_field.populate_grid(level)

        #if isLevelFinished():
        #    pass
        #    #level abbrechen

        ####################################################################################

    def iterate_game(self):
        pass


class Blocks(Image):
    pass

class GameField(GridLayout):
    def __init__(self, **kwargs):  
        super(GameField, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_grid_initial)

    def populate_grid_initial(self, abc):
        self.kivyrunner.loadLevel(1)
        level = self.kivyrunner.level

        self.populate_grid(level)

    def populate_grid(self, level):
        for x in xrange(level.size):
            for y in xrange(level.size):
                block = level.data[x][y]

                if block == '_':
                    source = IMAGEDIR + 'block_blank.png'

                elif block == '+':
                    source = IMAGEDIR + 'block_collectable.png'

                elif block == 'X':
                    source = IMAGEDIR + 'block_death.png'

                elif block == '#':
                    source = IMAGEDIR + 'block_wall.png'

                elif block == 'M':
                    source = IMAGEDIR + 'block_robot.png'

                else:
                    print('################ error - unknown item')
                    break

                a = (min(self.size) - 2*min(self.padding) - (10-1)*min(self.spacing))/10
                #print('################'+str(a))
                #a=30
                #self.add_widget(Blocks(source = source, size = (a, a), size_hint = (None, None)))
                b = Blocks(source = source, size_hint = (0.1, 0.1))
                self.add_widget(b)
                #b.size = [min(b.size)]*2

        # make a quadric grid
        
        #self.size = [min(self.size)]*2
        #self.size_hint = (None, None)


class BlackBoxLayout(BoxLayout):
    pass

class Item(Image):
    dnd_layout = ObjectProperty(None)
    blocktype = StringProperty()

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
                    black_box.clear_widgets()
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

        grid_1.clear_widgets()
        logic_boxes = self.kivyrunner.getLogicBoxes()

        for logic_box in logic_boxes:
            #item = Item(source=img_dir, size=(32, 32), size_hint=(None, None), dnd_layout = self)
            item = Item(source=IMAGEDIR + logic_box.picture, blocktype = logic_box.blocktype, dnd_layout = self)
            b = BlackBoxLayout()
            b.add_widget(item)
            grid_1.add_widget(b)

        n = grid_2.cols*grid_2.rows

        for i in range(n):
            b = BlackBoxLayout()
            #b.add_widget(Label(text='1'))
            grid_2.add_widget(b)

    def reset_logic(self):
        grid_2 = self.ids.grid_2
        for child in grid_2.children:
            child.clear_widgets()

class DnDApp(App):
    list_of_img_dirs = ListProperty()
    kivyrunner = ObjectProperty()

    def build(self):
        c = Builder.load_string(kv)
        self.kivyrunner = KivyRunner()

        #for i in IMAGES:
        #    self.list_of_img_dirs.append(IMAGEDIR + i)
            
        return c

if __name__ == "__main__":
    DnDApp().run()
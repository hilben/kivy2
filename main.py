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
from kivy.uix.relativelayout import RelativeLayout

from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color


from kivy.uix.button import Button

from kivy.clock import Clock
from kivy.properties import ListProperty, ObjectProperty, StringProperty

from kivy.lang import Builder

from kivy.uix.image import Image

from kivyrunner import KivyRunner
from logic import Logic

from os import listdir

from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter

from kivy.uix.screenmanager import ScreenManager, Screen

from logicblock import LogicBlock

IMAGEDIR = 'images/'

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
            Image:
                source: 'images/droid2.png'
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
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation:'vertical'
                size_hint_x: 0.5
                #Label:
                DnDLayout:
                    id: dnd
                #Label:
            BoxLayout:
                orientation:'vertical'
                size_hint_x: 0.5
                Label:
                GameField:
                    id: game_field
                Label:
        BoxLayout:
            size_hint_y: 0.1
            orientation: 'horizontal'
            Button:
                text: 'Home'
                on_press: root.manager.current = 'menu'
            Button:
                text: 'Go'
                on_press: root.start_game()
            Button:
                text: 'Stop'
                on_press: dnd.stop_logic()
            Button:
                text: 'Reset'
                on_press: dnd.reset_logic()
            Button:
                text: 'Previous'
                on_press: dnd.prev_level()
            Button:
                text: 'Next'
                on_press: dnd.next_level()


<GameField>:
    kivyrunner: app.kivyrunner
    size_hint: (None, None)
    size: min(self.parent.width, self.parent.height), min(self.parent.width, self.parent.height)
    cols: 10
    rows: 10
    padding: 2
    spacing: 2

<DnDLayout>:
    kivyrunner: app.kivyrunner
    size_hint: (None, None)
    size: min(self.parent.width, self.parent.height), min(self.parent.width, self.parent.height)
    BoxLayout:
        orientation: 'vertical'
        GridLayout:
            id: grid_1
            size_hint: (None, None)
            size: min(self.parent.width, self.parent.height), min(self.parent.width, self.parent.height)/9*3
            cols: 9
            rows: 3
            padding: 2
            spacing: 2

        GridLayout:
            id: grid_2
            size_hint: (None, None)
            size: min(self.parent.width, self.parent.height), min(self.parent.width, self.parent.height)
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


runRobot = False

class GameScreen(Screen):

    def start_game(self):
        logic_grid = self.ids.dnd.ids.grid_2

        size = logic_grid.rows
        logic = []

        for y in xrange(size):
            logic.append([])
            for x in xrange(size):
                logic[y].append(LogicBlock("","_"))

        index = size * size - 1

        for child in logic_grid.children:
            if not child.children:
                picture = 'block_blank.png'
                blocktype = '_'
                logic_block = LogicBlock(picture, blocktype)
            else:
                picture = child.children[0].source
                blocktype = child.children[0].blocktype
                logic_block = LogicBlock(picture, blocktype)


            print str(int(index/size)) + "  y: "+  str(size - ((index%size) - 1))
            logic[((index%size) )][int(index/size)] = logic_block
            index-=1

        for y in xrange(size):
            for x in xrange(size):
                print "blocktype: x:" + str(x) + " y: " + str(y) + " "  + str(logic[x][y].blocktype)

        logicobject = Logic(size,self.kivyrunner.level)
        logicobject.data = logic
        logicobject.printBlocks()
        self.kivyrunner.setLogic(logicobject)
        self.kivyrunner.logic.printBlocks()

        dt = 1#TODO

        global runRobot
        runRobot = True
        Clock.schedule_interval(self.iterate_game, dt)

    def iterate_game(self,time):

        global runRobot
        if runRobot == False:
            print "runRobot == false"
            Clock.unschedule(self.iterate_game)
        print "iterate!"
        self.kivyrunner.logic.printBlocks()
        #update level
        game_field = self.ids.game_field

        level = self.kivyrunner.level
        level.data = self.kivyrunner.getFieldData()

        game_field.clear_widgets()
        game_field.populate_grid(level)
        #do iteration
        self.kivyrunner.doIteration()
        #level abbrechen
        if self.kivyrunner.isLevelFinished():
            runRobot == False

        #draw pointers
        logic_grid = self.ids.dnd.ids.grid_2

        i = 0
        for child in logic_grid.children:

            x = int(i%6)
            y = int(i/6)
            print('x: '+str(x)+'   y:'+str(y) +'    '+ str(self.kivyrunner.logic.getPointerAt(x,y)))

            pointer = self.kivyrunner.logic.getPointerAt(x,y)
            if len(pointer) == 0:

                if child.children:
                    child.children[0].draw_pointer('*')
            i+=1


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
        for y in xrange(level.size):
            for x in xrange(level.size):
                block = level.data[x][y]

                if block == '_':
                    source = IMAGEDIR + 'block_blank.png'

                elif block == '#':
                    source = IMAGEDIR + 'block_collectable.png'

                elif block == 'X':
                    source = IMAGEDIR + 'block_death.png'

                elif block == '+':
                    source = IMAGEDIR + 'block_wall.png'

                elif block == 'M':
                    source = IMAGEDIR + 'block_robot.png'

                else:
                    print('################ error - unknown item')
                    break

                a = (min(self.size) - 2*min(self.padding) - (10-1)*min(self.spacing))/10
                b = Blocks(source = source, size_hint = (0.1, 0.1))
                self.add_widget(b)

class BlackBoxLayout(BoxLayout):
    pass

class DragableItem(Image):
    dnd_layout = ObjectProperty(None)
    blocktype = StringProperty()

class Item(Image):
    dnd_layout = ObjectProperty(None)
    blocktype = StringProperty()

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        is_pointed_at = False

    def on_touch_down(self, touch, *args):
        #global runRobot
        if self.collide_point(*touch.pos) and not runRobot: #if it is touched on
            touch.grab(self)
            self.scatter = Scatter(center = touch.pos, size= self.size, size_hint=(None, None), auto_bring_to_front = True)
            self.scatter.add_widget(DragableItem(source = self.source, blocktype = self.blocktype, dnd_layout = self.dnd_layout))
            self.dnd_layout.add_widget(self.scatter)
            return True

        return super(Item, self).on_touch_down(touch, *args)

    def on_touch_move(self, touch, *args):
        grid_1 = self.dnd_layout.ids.grid_1
        grid_2 = self.dnd_layout.ids.grid_2

        if touch.grab_current == self:
            self.scatter.center = touch.pos

            #if not self.dnd_layout.collide_point(*touch.pos):
            #    self.dnd_layout.remove_widget(self.scatter)

    def on_touch_up(self, touch, *args):
        grid_1 = self.dnd_layout.ids.grid_1
        grid_2 = self.dnd_layout.ids.grid_2

        check = False

        if touch.grab_current == self:
            for black_box in grid_2.children:
                if black_box.collide_point(*touch.pos):
                    black_box.clear_widgets()
                    black_box.add_widget(ItemMove(source = self.source, blocktype = self.blocktype, dnd_layout = self.dnd_layout))
                    self.dnd_layout.remove_widget(self.scatter)
                    check = True
            if not grid_2.collide_point(*touch.pos) or check==False:
                self.dnd_layout.remove_widget(self.scatter)

    def draw_pointer(self, pointer):
        if pointer == True and self.is_pointed_at == False:
            r = 0
            g = 1
            b = 0
            d = 0.2

            self.is_pointed_at = True

            with self.canvas:
                self.color = Color(r, g, b, .2, mode='rgba')
                Rectangle(pos=self.pos, size=self.size)

        if pointer == False:
            r = 0
            g = 0
            b = 1
            d = 0.2

        if pointer == '***':
            r = 1
            g = 0
            b = 0
            d = 0.2


        #self.canvas.clear()
        #with self.canvas.after:


class ItemMove(Item):
    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos) and not runRobot: #if it is touched on
            touch.grab(self)
            self.parent.remove_widget(self)
            self.scatter = Scatter(center = touch.pos, size= self.size, size_hint=(None, None), auto_bring_to_front = True)
            self.scatter.add_widget(DragableItem(source = self.source, blocktype = self.blocktype, dnd_layout = self.dnd_layout))
            self.dnd_layout.add_widget(self.scatter)
            return True
        return super(Item, self).on_touch_down(touch, *args)


class DnDLayout(RelativeLayout):

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
	global runRobot
	runRobot = False
        grid_2 = self.ids.grid_2
        for child in grid_2.children:
            child.clear_widgets()
	self.kivyrunner.reset()

    def stop_logic(self):
        global runRobot
        runRobot = False
        self.kivyrunner.reset()


    def prev_level(self):
        global runRobot
        runRobot = False
        self.kivyrunner.reset()
        self.kivyrunner.previousLevel()

    def next_level(self):
        global runRobot
        runRobot = False
        self.kivyrunner.reset()
        self.kivyrunner.nextLevel()

class DnDApp(App):
    list_of_img_dirs = ListProperty()
    kivyrunner = ObjectProperty()

    def build(self):
        c = Builder.load_string(kv)
        self.kivyrunner = KivyRunner()
        return c

if __name__ == "__main__":
    DnDApp().run()

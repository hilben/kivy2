from kivy.app import App
#from kivy.garden.magnet import Magnet
from magnet import Magnet

from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from os import listdir

from kivy.graphics import Color, Line, Rectangle
 
#IMAGEDIR = '/usr/share/icons/hicolor/32x32/apps/'
IMAGEDIR = 'pics/'
 

IMAGES = filter(
    lambda x: x.endswith('.png'),
    listdir(IMAGEDIR))

class Test(FloatLayout):
    def copy(self):
        pass


class GridLabel(Label):
    pass


class GridLayoutWithGrid(GridLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(GridLayout, self).__init__(**kwargs)
    #     self.canvas.add(Color(1,1,0))
    #     self.canvas.add(Rectangle(pos=(0,0),size=self.size))
    #     for i in range(3):
    #         self.add_widget(GridLabel())
        # with self.canvas.before:
        #     Color(1, 0, .4, mode='rgb')
        #     Line(points=(self.pos) + [self.pos[0], self.pos[0]+self.size[0]],width=3)
        #     #Line(points=((self.pos) + [self.pos[0], self.pos[0]+self.size[0]]),width=3)
        # with self.canvas:
        #     Color(0, 1, .4, mode='rgb')
        #     Line(points=(self.pos) + [self.pos[0], self.pos[0]+self.size[0]],width=3)
        #     print('#######################################'+str(self.pos))
        # with self.canvas.after:
        #     Color(0, 1, .4, mode='rgb')
        #     Line(points=(self.pos) + [self.pos[0], self.pos[0]+self.size[0]],width=3)
        #     print('#######################################'+str(self.pos))

class DraggableLabel(Magnet):
    app = ObjectProperty(None)


class DraggableImage(Magnet):
    img = ObjectProperty(None, allownone=True)
    app = ObjectProperty(None)
 
    def on_img(self, *args):
        self.clear_widgets()
 
        if self.img:
            Clock.schedule_once(lambda *x: self.add_widget(self.img), 0)
 
    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.remove_widget(self.img)
            self.app.root.add_widget(self.img)
            self.center = touch.pos
            self.img.center = touch.pos
            return True
 
        return super(DraggableImage, self).on_touch_down(touch, *args)
 
    def on_touch_move(self, touch, *args):
        grid_layout = self.app.root.ids.grid_layout
        float_layout = self.app.root.ids.float_layout
 
        if touch.grab_current == self:
            self.img.center = touch.pos
            if grid_layout.collide_point(*touch.pos):
                grid_layout.remove_widget(self)
                float_layout.remove_widget(self)
 
                for i, c in enumerate(grid_layout.children):
                    if c.collide_point(*touch.pos):
                        grid_layout.add_widget(self, i - 1)
                        break
                else:
                    grid_layout.add_widget(self)
            else:
                if self.parent == grid_layout:
                    grid_layout.remove_widget(self)
                    float_layout.add_widget(self)
 
                self.center = touch.pos
 
        return super(DraggableImage, self).on_touch_move(touch, *args)
 
    def on_touch_up(self, touch, *args):
        if touch.grab_current == self:
            self.app.root.remove_widget(self.img)
            self.add_widget(self.img)
            touch.ungrab(self)
            return True
 
        return super(DraggableImage, self).on_touch_up(touch, *args)
 
 
class KivyRunnerApp(App):
    def build(self):
        for i in IMAGES:
            image = Image(source=IMAGEDIR + i, size=(32, 32),
                          size_hint=(None, None))
            draggable = DraggableImage(img=image, app=self,
                                       size_hint=(None, None),
                                       size=(32, 32))
            self.root.ids.grid_layout.add_widget(draggable)
        
        cols = self.root.ids.float_layout.cols
        rows = self.root.ids.float_layout.rows
        number = cols*rows
        #number = 50
        #self.root.ids.float_layout.add_widget(Label(text=str(number)))
        #self.root.ids.float_layout.add_widget(Label(text=str(number+20)))

        for i in range(number):
            self.root.ids.float_layout.add_widget(GridLabel(text=str(i+1)))

        for i in range(12):
            self.root.ids.grid1.add_widget(GridLabel(text='Item '+ str(i+1)))

        for i in range(36):
            self.root.ids.grid2.add_widget(GridLabel())

        return self.root
 
 
if __name__ == '__main__':
    KivyRunnerApp().run()
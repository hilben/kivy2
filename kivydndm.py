from kivy.app import App
from magnet import Magnet
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

import copy

from os import listdir

IMAGEDIR = 'kivy/pics/'

IMAGES = filter(
    lambda x: x.endswith('.png'),
    listdir(IMAGEDIR))

kv = '''
FloatLayout:
    BoxLayout:
        GridLayout:
            id: grid_layout_1
            cols: 5

        GridLayout:
            id: grid_layout_2
            cols: 5
            #id: float_layout
            
'''


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
            #a = copy.copy(self.img)
            #self.app.root.add_widget(a)
            self.app.root.add_widget(self.img)
            self.center = touch.pos
            self.img.center = touch.pos
            return True

        return super(DraggableImage, self).on_touch_down(touch, *args)

    def on_touch_move(self, touch, *args):
        grid_layout_1 = self.app.root.ids.grid_layout_1
        grid_layout_2 = self.app.root.ids.grid_layout_2

        if touch.grab_current == self:
            self.img.center = touch.pos
            if grid_layout_1.collide_point(*touch.pos): #wenn es in grid_layout_1 1 ist
                grid_layout_1.remove_widget(self)
                grid_layout_2.remove_widget(self)
                print('2131354684616135151')

                for i, c in enumerate(grid_layout_1.children):
                    if c.collide_point(*touch.pos):
                        grid_layout_1.add_widget(self, i - 1)
                        break
                else:
                    grid_layout_1.add_widget(self)
            else:
                if self.parent == grid_layout_1:
                    grid_layout_1.remove_widget(self)
                    #grid_layout_2.add_widget(self)
                    #grid_layout_2.add_widget(Label(text='123'))
                    #grid_layout_2.add_widget(self.img)
                    print('Asdfasdfasdfasdfasdfasdfasdf')

                self.center = touch.pos

        return super(DraggableImage, self).on_touch_move(touch, *args)

    def on_touch_up(self, touch, *args):
        if touch.grab_current == self:
            self.app.root.remove_widget(self.img)
            self.add_widget(self.img)
            touch.ungrab(self)
            print('#####################')
            return True

        return super(DraggableImage, self).on_touch_up(touch, *args)


class DnDMagnet(App):
    def build(self):
        self.root = Builder.load_string(kv)
        for i in IMAGES:
            image = Image(source=IMAGEDIR + i, size=(32, 32),
                          size_hint=(None, None))
            draggable = DraggableImage(img=image, app=self,
                                       size_hint=(None, None),
                                       size=(32, 32))
            self.root.ids.grid_layout_1.add_widget(draggable)

        return self.root


if __name__ == '__main__':
    DnDMagnet().run()
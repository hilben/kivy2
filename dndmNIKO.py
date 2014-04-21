from kivy.app import App
#from kivy.garden.magnet import Magnet
from magnet import Magnet

from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
 
from os import listdir
 
#IMAGEDIR = '/usr/share/icons/hicolor/32x32/apps/'
IMAGEDIR = 'pics/'
 

IMAGES = filter(
    lambda x: x.endswith('.png'),
    listdir(IMAGEDIR))

#print(IMAGES)
 
kv = '''
BoxLayout:
    orientation:'vertical'
    TabbedPanel:
        do_default_tab: False
        size_hint_y: None
        size: 0,150

        TabbedPanelItem:
            text: 'Logic Bricks'
            GridLayout:
                #orientation:'horizontal'
                #rientation:'vertical'
                id: grid_layout
                cols: int(self.width / 32)

        TabbedPanelItem:
            text: 'Level Bricks'
            GridLayout:
                #orientation:'horizontal'
                #rientation:'vertical'
                id: grid_layout2
                cols: int(self.width / 32)
    BoxLayout:
        GridLayout:
            id: float_layout
            cols: int(self.width / 32)
            #canvas:
            #   Color:
            #       rgb: 150, 0, 150
            #    Rectangle:
            #        size: self.size
        GridLayout:
            id: float_layout2
            cols: int(self.width / 32)
            #canvas:
            #    Color:
            #        rgb: 150, 0, 150
            #    Rectangle:
            #        size: self.size
    ControlBar

<ControlBar@BoxLayout>:
    size_hint_y: None
    size: 0,60
    padding: 10
    spacing: 10
    
    BoxLayout:
        spacing: 10
        ToggleButton:
            text: 'Play'
            size_hint_x: None
            size: 100,0
        ToggleButton:
            text: 'Freeze'
            size_hint_x: None
            size: 100,0
        ToggleButton:
            text: 'Blackout'
            size_hint_x: None
            size: 100,0
        ToggleButton:
            text: 'Random'
            size_hint_x: None
            size: 100,0
    
        Slider:
            id: slider_global_speed
            size_hint_x: None
            size: 250,0
            min: 0
            max: 5
            value: 1
            step: 0.01
            on_value: textinput_global_speed.text = str(self.value*100)
        TextInput:
            id: textinput_global_speed
            size_hint_x: None
            size: 50,0
            multiline: False
            on_text_validate: slider_global_speed.value = float(self.text)/100

            text: '100'
        Label:
            size_hint_x: None
            size: 20,0
            text: '%'
        Label:
        Button:
            size_hint_x: None
            size: 50,0
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
 
 
class DnDMagnet(App):
    def build(self):
        self.root = Builder.load_string(kv)
        for i in IMAGES:
            image = Image(source=IMAGEDIR + i, size=(32, 32),
                          size_hint=(None, None))
            draggable = DraggableImage(img=image, app=self,
                                       size_hint=(None, None),
                                       size=(32, 32))
            self.root.ids.grid_layout.add_widget(draggable)
 
        return self.root
 
 
if __name__ == '__main__':
    DnDMagnet().run()
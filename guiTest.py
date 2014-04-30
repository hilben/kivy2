from kivy.app import App
from magnet import Magnet
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.properties import NumericProperty, ListProperty, DictProperty, StringProperty

from os import listdir

kv = '''
FloatLayout:
    BoxLayout:
        GridLayout:
            id: grid_layout
            cols: int(self.width / 32)
            Button:

        GridLayout:
            id: float_layout
        MyBoxLayout:
        #MyBoxLayout:

<MyBoxLayout>:
    id: asdfasdfasdf
    blubber: 15
    a:
    b: str(self.blubber)
    BoxLayout:
        id: asdf
    Label:
        text: '123'

    Label:
        text: str(root.blubber)

'''
def blubber2():
    print('############################## it works')

class MyBoxLayout(BoxLayout):
    blubber = NumericProperty(1)
    b = StringProperty()
    a = blubber2()

    def __init__(self, **kwargs):  
        super(MyBoxLayout, self).__init__(**kwargs)
        #super(self).__init__(**kwargs)
        
        self.blubber = 123513
        #for i in list:
        print "asdsadasdasdasd" + str(self.b)

        print "###################" + str(self.b)
        self.add_widget(Label(text = 'a,'))
        self.add_widget(Label(text = 'b,'))


    

    

class DnDMagnet(App):
    def build(self):
        self.root = Builder.load_string(kv)

        return self.root


if __name__ == '__main__':
    DnDMagnet().run()
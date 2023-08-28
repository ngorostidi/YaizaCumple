from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file('boxes.kv')

class MyLayout(Widget):

    def animate_it(self, widget, *args):
        animate = Animation(
                background_color = (123/255, 8/255, 1/255, 1),
                duration=2)

        animate.start(widget)

        animate += Animation(
                background_color = (0.2, 0.8, 0.2, 0.8),
                duration=0.1)
        
        animate.start(widget)

class Cazador(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Cazador().run()

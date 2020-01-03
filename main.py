import kivy
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget

t1 = SoundLoader.load('mobilemagaphone_im-smart.mp3')
t2 = SoundLoader.load('mobilemagaphone_china.mp3')
t3 = SoundLoader.load('mobilemagaphone_congradulations.mp3')
t4 = SoundLoader.load('russia-russia-russia.mp3')
t5 = SoundLoader.load('mobilemagaphone_fake_news.mp3')
t6 = SoundLoader.load('400lb-hacker.mp3')
t7 = SoundLoader.load('mobilemagaphone_you-are-fake_news.mp3')
t8 = SoundLoader.load('mobilemagaphone_dont-be-rude.mp3')
t9 = SoundLoader.load('mobilemagaphone_shes-smart.mp3')
t10 = SoundLoader.load('yuuge.mp3')


class Ta(ButtonBehavior, Image):
    def on_press(self):
        # dont be rude
        t8.play()


class Tb(ButtonBehavior, Image):
    def on_press(self):
        t2.play()


class Tc(ButtonBehavior, Image):
    def on_press(self):
        t4.play()


class Td(ButtonBehavior, Image):
    def on_press(self):
        # Congradulations
        t3.play()


class Te(ButtonBehavior, Image):
    def on_press(self):
        t5.play()


class Tf(ButtonBehavior, Image):
    def on_press(self):
        t10.play()


class Tg(ButtonBehavior, Image):
    def on_press(self):
        t7.play()


class Th(ButtonBehavior, Image):
    def on_press(self):
        t6.play()

class Ti(ButtonBehavior, Image):
    def on_press(self):
        t9.play()

class Tj(ButtonBehavior, Image):
    def on_press(self):
        t1.play()


class MyGrid(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()



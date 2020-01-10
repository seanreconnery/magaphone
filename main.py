import kivy
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget

t8 = SoundLoader.load('assets/mobilemagaphone_dont-be-rude.wav')
t2 = SoundLoader.load('assets/mobilemagaphone_china.wav')
t4 = SoundLoader.load('assets/russia-russia-russia.wav')
t3 = SoundLoader.load('assets/mobilemagaphone_congradulations.wav')
t5 = SoundLoader.load('assets/mobilemagaphone_fake_news.wav')
t10 = SoundLoader.load('assets/yuuge.wav')
t7 = SoundLoader.load('assets/mobilemagaphone_you-are-fake_news.wav')
t6 = SoundLoader.load('assets/400lb-hacker.wav')
t9 = SoundLoader.load('assets/mobilemagaphone_shes-smart.wav')
t1 = SoundLoader.load('assets/mobilemagaphone_im-smart.wav')


class Ta(ButtonBehavior, Image):
    def on_press(self):
        t8.play()

class Tb(ButtonBehavior, Image):
    def on_press(self):
        t2.play()

class Tc(ButtonBehavior, Image):
    def on_press(self):
        t4.play()

class Td(ButtonBehavior, Image):
    def on_press(self):
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

class MAGAphone(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MAGAphone().run()

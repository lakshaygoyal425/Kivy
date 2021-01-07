from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        image = Image(source='IMG_20191113_175920_776.jpg')
        return image


MainApp().run()

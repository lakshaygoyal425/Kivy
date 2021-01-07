from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)


class MainApp(App):
    def build(self):
        label = Label(text="This is IRONMAN", font_size='20sp', bold=True, italic=True, color=(1, 0, 0))
        return label


MainApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import AsyncImage

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=110, padding=80)
        img = AsyncImage(source='http://kivy.org/logos/kivy-logo-black-64.png')
        button = Button(text='LOGIN', size_hint=(None, None), width=100, height=100,
                        pos_hint={'center_x': 0.5})
        layout.add_widget(img)
        layout.add_widget(button)
        return layout


MainApp().run()

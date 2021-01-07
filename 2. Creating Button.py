from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        button = Button(text="Print this", size_hint=(0.2, 0.2), font_size='20sp', bold=True,
                        italic=True, pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        on_press=self.printpress,
                        on_release=self.printrelease
                        )
        return button

    def printpress(self, obj):
        print("Button Has Been Pressed")

    def printrelease(self, obj):
        print("Button Has Been Released")


MainApp().run()

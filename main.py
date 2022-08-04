from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (300, 500)

switchs = """
MDSwitch:
    pos_hint: {'center_x': .5, 'center_y': .5}
    width: dp(45)
    on_active: app.check(*args)
"""

class MyApp(MDApp):
    def build(self):
        switch = Builder.load_string(switchs)
        self.theme_cls.theme_style = "Light"
        return switch
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

MyApp().run()
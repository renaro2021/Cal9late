from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.app import App

class Calc(App):
    def build(self):
        Window.maximize()
        Window.bind(on_resize=self.windowresize)
        self.endb = None
        self.enda=None
        self.pass2 = ""
        self.calcs = ["+","-","*","/"]
        self.solution=TextInput(foreground_color="black",background_color="white",halign="right",font_size=150,height=55,readonly=True,multiline=True)
        self.mainpage=BoxLayout(orientation="vertical")
        self.mainpage.add_widget(self.solution)
        chars=[["/",".","0","C"],
                   ["*","7","8","9"],
                   ["-","4","5","6"],
                   ["+","1","2","3"],]
        for row in chars:
            spage=BoxLayout()
            for label in row:
                if label in self.calcs:
                    click=Button(text=label,pos_hint={"center_x":0.5,"center_y":0.5},background_color="limegreen",background_normal="",font_size=60,) 
                else:
                    click=Button(text=label,pos_hint={"center_x":0.5,"center_y":0.5},background_color="black",background_normal="",font_size=60)
                click.bind(on_press=self.pressing)
                spage.add_widget(click)
            self.mainpage.add_widget(spage)
        equals=Button(
            text="=",font_size=60,background_color="limegreen",background_normal="",
            pos_hint={"center_x":0.5,"center_y":0},
            size_hint=(1, 0.8)
        )
        equals.bind(on_press=self.results)
        self.mainpage.add_widget(equals)
        return self.mainpage 
    
    def results(self,instance):   
        try:
            chars = self.solution.text
            if chars:
                over = str(round(eval(self.solution.text), 5))
                self.solution.text = over
        except (SyntaxError, ZeroDivisionError, NameError):
            self.solution.text = "Error"

    def windowresize(self, window, width, height, *args):
     if width > height:
        Window.orientation = 'landscape'
     else:
        Window.orientation = 'portrait'
        
    def pressing(self,instance):
        r = self.solution.text
        charb = instance.text
        if charb=="C":
            self.solution.text=""
            self.pass2 = ""
        else:
            if r and (self.endb and charb in self.calcs):
                return
            elif r=="" and charb in self.calcs:
                return
            else:
                solid=r+charb
                self.solution.text=solid
                self.pass2 += charb
        self.enda=charb
        self.endb=self.enda in self.calcs

if __name__ == "__main__":
    Calc().run() 

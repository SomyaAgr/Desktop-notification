# DRINKING WATER NOTIFICATION
import time
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import notification


class DrinkingLayout(GridLayout):
    def __init__(self,**kwargs):
        super(DrinkingLayout,self).__init__()
        self.cols=2
        self.add_widget(Label(text="ENTER YOUR NAME:"))
        self.s_name=TextInput()
        self.add_widget(self.s_name)
        self.add_widget(Label(text="ENTER YOUR GENDER:"))
        self.s_Gender = TextInput()
        self.add_widget(self.s_Gender)
        self.add_widget(Label(text="ENTER YOUR Age:"))
        self.s_Age = TextInput()
        self.add_widget(self.s_Age)
        self.press=Button(text="Enter")
        self.press.bind(on_press=self.enter)
        self.add_widget(self.press)

    def enter(self,instance):
        print("The details u have entered is "+self.s_name.text +" of "+self.s_Age.text +" "+ self.s_Gender.text)



class DrinkingApp(App):
    def build(self):
        return DrinkingLayout()

if __name__ == '__main__':

    DrinkingApp().run()
    notification.notify(
        title ="PLEASE DRINK WATER now !! ",
        message =" Drink approx. 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women",
        app_icon="D:\PROJECT\Drinking_Water_Notification\Icon.ico",
        timeout=2
            )

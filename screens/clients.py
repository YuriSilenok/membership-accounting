from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.dropdown import DropDown


class Clients(Screen):

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'welcome'

    def spinner_clicked(self, value):
        self.ids.spinner_id.text = value

    

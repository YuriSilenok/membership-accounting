from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from MakeGoogleSheets import spreadsheetId

class Clients(Screen):

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'welcome'


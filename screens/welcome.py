from kivy.uix.screenmanager import Screen, SlideTransition
from kivyauth.utils import auto_login, login_providers
from kivyauth.google_auth import login_google
from kivy import platform


class Welcome(Screen):

    # def on_start(self):
    #     if auto_login(login_providers.google):
    #         self.current_provider = login_providers.google

    def login(self):
        print('login')
        login_google()

    def after_login(self, **qwargs):
        print('after_login')

    def error_listener(self, **qwargs):
        print('error_listener')
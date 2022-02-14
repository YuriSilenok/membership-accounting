import os

from kivy import platform
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivyauth.google_auth import initialize_google

from screens.welcome import Welcome
from screens.clients import Clients

# GOOGLE_CLIENT_ID = '.apps.googleusercontent.com'

GOOGLE_CLIENT_ID = '.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = ''

class MembershipAccounting(App):

    def build(self):
        if platform == 'android':
            initialize_google(self.after_login, self.error_listener)
        else:
            initialize_google(
                self.after_login,
                self.error_listener,
                GOOGLE_CLIENT_ID,
                GOOGLE_CLIENT_SECRET,
            )
        sm = ScreenManager()

        Builder.load_file(os.path.join(os.getcwd(), 'designs', 'welcome.kv'))
        sm.add_widget(Welcome(name='welcome'))

        Builder.load_file(os.path.join(os.getcwd(), 'designs', 'clients.kv'))
        sm.add_widget(Clients(name='clients'))

        return sm

    def after_login(self, **qwargs):
        print('after_login')

    def error_listener(self, **qwargs):
        print('error_listener')


if __name__ == '__main__':
    MembershipAccounting().run()

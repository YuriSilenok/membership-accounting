import os

from kivy import platform
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivyauth.google_auth import initialize_google

from screens.welcome import Welcome
from screens.clients import Clients

ANDROID_GOOGLE_CLIENT_ID = os.getenv('ANDROID_GOOGLE_CLIENT_ID')

WEB_GOOGLE_CLIENT_ID = os.getenv('WEB_GOOGLE_CLIENT_ID')
WEB_GOOGLE_CLIENT_SECRET = os.getenv('WEB_GOOGLE_CLIENT_SECRET')


class MembershipAccounting(App):

    def build(self):
        if platform == 'android':
            initialize_google(self.after_login, self.error_listener, ANDROID_GOOGLE_CLIENT_ID)
        else:
            initialize_google(
                self.after_login,
                self.error_listener,
                WEB_GOOGLE_CLIENT_ID,
                WEB_GOOGLE_CLIENT_SECRET,
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

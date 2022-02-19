import os

from kivy import platform
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.welcome import Welcome
from screens.clients import Clients


class MembershipAccounting(App):

    def build(self):
        sm = ScreenManager()

        Builder.load_file(os.path.join(os.getcwd(), 'designs', 'welcome.kv'))
        sm.add_widget(Welcome(name='welcome'))

        Builder.load_file(os.path.join(os.getcwd(), 'designs', 'clients.kv'))
        sm.add_widget(Clients(name='clients'))

        return sm


if __name__ == '__main__':
    MembershipAccounting().run()

import os

from kivy.uix.screenmanager import Screen, SlideTransition
from kivyauth.google_auth import login_google
from kivy import platform
from kivyauth.utils import auto_login, login_providers


class Welcome(Screen):

    def on_enter(self):
        if platform == 'android':
            if auto_login(login_providers.google):
                self.current_provider = login_providers.google
                self.go_to_clients()
            else:
                from kivyauth.android.google_auth import initialize_google

                android_google_client_id = os.getenv('ANDROID_GOOGLE_CLIENT_ID')
                initialize_google(self.after_login, self.error_listener, android_google_client_id)
        else:
            from kivyauth.desktop.google_auth import initialize_google

            web_google_client_id = os.getenv('WEB_GOOGLE_CLIENT_ID')
            web_google_client_secret = os.getenv('WEB_GOOGLE_CLIENT_SECRET')
            initialize_google(
                self.after_login,
                self.error_listener,
                web_google_client_id,
                web_google_client_secret,
            )

    def login(self):
        login_google()

    def after_login(self, user_name, user_email, user_logo):
        self.go_to_clients()

    def go_to_clients(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'clients'

    def error_listener(self, *args, **qwargs):
        print('error_listener', args, qwargs)

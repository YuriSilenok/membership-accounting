from kivy.uix.screenmanager import Screen, SlideTransition
from kivyauth.utils import auto_login, login_providers
from kivyauth.google_auth import initialize_google


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Welcome(Screen):
    def login_and_create_folder(self):

        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
    # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)

        folder_metadata = {
            'title': 'membership-accounting',
            # The mimetype defines this new file as a folder, so don't change this.
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        if folder['id']:
            self.manager.current = 'clients'
        folder_id = folder['id']
        emaill = folder['lastModifyingUser']['emailAddress']
        file5 = drive.CreateFile({'parents': [{'id': f'{folder_id}'}],
                                  'title': f'{emaill}'})
        # Read file and set it as a content of this instance.
        file5.SetContentFile('Sheets.xlsx')
        file5.Upload()  # Upload the file.
        print({emaill: file5['id']})

        return {emaill: file5['id']}



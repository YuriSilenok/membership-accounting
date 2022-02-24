import gspread
from kivy.uix.screenmanager import Screen


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Welcome(Screen):
    def login_and_create_folder(self):
        gauth = GoogleAuth() #Костыль на авторизацию
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        folder_metadata = {
            'title': 'membership-accounting',
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        folder_id = folder['id']
        emaill = folder['lastModifyingUser']['emailAddress']
        file = drive.CreateFile({'parents': [{'id': f'{folder_id}'}],
                                 'title': f'{emaill}',
                                 'mimeType': 'application/vnd.google-apps.spreadsheet'})

        file.Upload()
        file_id = file['id']

        permission = file.InsertPermission({
            'type': 'anyone',
            'value': 'anyone',
            'role': 'writer'})
        print(folder['alternateLink'])

        gs = gspread.service_account(filename='fileapi.json')
        sht = gs.open_by_key(f'{file_id}')
        worksheet1 = sht.add_worksheet(title="Клиенты", rows="200", cols="8")
        worksheet1.update('A1:H1', [["Идентификатор клиента",
                                     "Дата регистации",
                                     "Фамилия",
                                     "Имя",
                                     "Отчество",
                                     "Номер телефона",
                                     "Количество абонементов",
                                     "Дата покупки последенго абонемента"]])

        worksheet2 = sht.add_worksheet(title="Абонементы", rows="200", cols="7")
        worksheet2.update('A1:G1', [["Идентификатор абонемента",
                                     "Идентификатор клиента",
                                     "Дата создания",
                                     "Цена абонемента",
                                     "Количесво занятий",
                                     "Пройденных занятий",
                                     "Дата и время последней тренировки"]])

        worksheet3 = sht.add_worksheet(title="Тренировки", rows="200", cols="3")
        worksheet3.update('A1:C1', [["Идентификатор тренировки",
                                     "Идентификатор абонемента",
                                     "Дата и время тренировки"],
                                    ])
        worksheet = sht.sheet1
        sht.del_worksheet(worksheet)

        worksheet1.format('A1:H200', {'wrapStrategy': 'LEGACY_WRAP'})
        worksheet2.format('A1:G200', {'wrapStrategy': 'LEGACY_WRAP'})
        worksheet3.format('A1:C200', {'wrapStrategy': 'LEGACY_WRAP'})


        print('Код выполнен успешно')
        self.folder_id = ""
        return {emaill: file['id']}

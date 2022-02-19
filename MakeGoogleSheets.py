from pprint import pp, pprint
import httplib2
import apiclient.discovery

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

CREDENTIALS_FILE = 'fileapi.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               [
                                                                   'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API


def created():
    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Google sheets', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Клиенты',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}},
                   {'properties': {'sheetType': 'GRID',
                                   'sheetId': 1,
                                   'title': 'Абонементы',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}},
                   {'properties': {'sheetType': 'GRID',
                                   'sheetId': 2,
                                   'title': 'Тренировки',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}}
                   ]
    }).execute()
    print('https://docs.google.com/spreadsheets/d/' + spreadsheet['spreadsheetId'])
    spreadsheetId = spreadsheet['spreadsheetId']  # сохраняем идентификатор файла
    print(f'Sheet id = {spreadsheetId}')
    return spreadsheetId


def dostup(spreadsheetId):
    emaill = 'denischaginnn@gmail.com'

    driveService = apiclient.discovery.build('drive', 'v3',
                                             http=httpAuth)  # Выбираем работу с Google Drive и 3 версию API
    driveService.permissions().create(
        fileId=spreadsheetId,
        body={'type': 'user', 'role': 'writer', 'emailAddress': f'{emaill}'},  # Открываем доступ на редактирование
        fields='id'
    ).execute()


def batchupdated(spreadsheetId):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        # Данные воспринимаются, как вводимые пользователем (считается значение формул)

        "data": [
            {"range": "Клиенты!A1:H1",
             "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
             "values": [
                 ['Идентификатор клиента',
                  "Дата регистрации",
                  "Фамилия",
                  "Имя",
                  "Отчество",
                  "Номер телефона",
                  "Количество абонементов",
                  "Дата покупки последнего абонемента"],  # Заполняем 1ую строку
             ]},
            {"range": "Абонементы!A1:G1",
             "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
             "values": [
                 ["Идентификатор абонемента",
                  "Идентификатор клиента",
                  "Дата создания",
                  "Цена абонемента",
                  "Количесво занятий",
                  "Пройденных занятий",
                  "Дата и время последней тренировки"],  # Заполняем 1ую строку
             ]},
            {"range": "Тренировки!A1:C1",
             "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
             "values": [
                 ["Идентификатор тренировки",
                  "Идентификатор абонемента",
                  "Дата и время тренировки"],  # Заполняем 1ую строку
             ]},
        ],
    }).execute()


# results = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body={
#     "requests": [
#
#         {
#             "DeleteRange":
#                 {
#                     "range": {
#                         "A1:D1"
#                     },
#                     "shiftDimension": "COLUMNS"
#                 }
#         },
#     ]
# }).execute()
def geting(spreadsheetId):
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId,
        range='A1:E10',
        majorDimension='ROWS'
    ).execute()
    pprint(values)


def login_and_create_folder():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    print(gauth)  # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)

    folder_metadata = {
        'title': 'membership-accounting',
        # The mimetype defines this new file as a folder, so don't change this.
        'mimeType': 'application/vnd.google-apps.folder'

    }

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    folder_id = folder['id']
    pprint(folder)
    emaill = folder['lastModifyingUser']['emailAddress']
    file5 = drive.CreateFile({'parents': [{'id': f'{folder_id}'}],
                              'title': f'{emaill}'})
    # Read file and set it as a content of this instance.
    file5.SetContentFile('Sheets.xlsx')
    file5.Upload()  # Upload the file.

    return {emaill:file5['id']}



if __name__ == '__main__':
    print(login_and_create_folder())


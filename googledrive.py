from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

folder_metadata = {
    'title' : 'New folder',
    # The mimetype defines this new file as a folder, so don't change this.
    'mimeType' : 'application/vnd.google-apps.folder'
}
folder = drive.CreateFile(folder_metadata)
folder.Upload()
print(folder, folder_metadata)

GoogleDriveFile({'title': 'New folder', 'mimeType': 'application/vnd.google-apps.folder', 'kind': 'drive#file', 'id': '1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb', 'etag': '"MTY0NTI1MzMyNzc4Nw"', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb', 'alternateLink': 'https://drive.google.com/drive/folders/1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb', 'embedLink': 'https://drive.google.com/embeddedfolderview?id=1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb', 'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/application/vnd.google-apps.folder+48', 'labels': {'starred': False, 'hidden': False, 'trashed': False, 'restricted': False, 'viewed': True}, 'copyRequiresWriterPermission': False, 'createdDate': '2022-02-19T06:48:47.787Z', 'modifiedDate': '2022-02-19T06:48:47.787Z', 'modifiedByMeDate': '2022-02-19T06:48:47.787Z', 'lastViewedByMeDate': '2022-02-19T06:48:47.787Z', 'markedViewedByMeDate': '1970-01-01T00:00:00.000Z', 'version': '1', 'parents': [{'kind': 'drive#parentReference', 'id': '0AA9JPxWhxbHNUk9PVA', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb/parents/0AA9JPxWhxbHNUk9PVA', 'parentLink': 'https://www.googleapis.com/drive/v2/files/0AA9JPxWhxbHNUk9PVA', 'isRoot': True}], 'userPermission': {'kind': 'drive#permission', 'etag': '"KY0h8FVnE1G5bVxerB0oDZANAQ8"', 'id': 'me', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1PbiQvd7ViKHV2te79XphGrqPAvLBbPQb/permissions/me', 'role': 'owner', 'type': 'user', 'pendingOwner': False}, 'quotaBytesUsed': '0', 'ownerNames': ['Чагин Денис'], 'owners': [{'kind': 'drive#user', 'displayName': 'Чагин Денис', 'picture': {'url': 'https://lh3.googleusercontent.com/a/default-user=s64'}, 'isAuthenticatedUser': True, 'permissionId': '01000335872267204118', 'emailAddress': 'chagin.deniskpc772020@gmail.com'}], 'lastModifyingUserName': 'Чагин Денис', 'lastModifyingUser': {'kind': 'drive#user', 'displayName': 'Чагин Денис', 'picture': {'url': 'https://lh3.googleusercontent.com/a/default-user=s64'}, 'isAuthenticatedUser': True, 'permissionId': '01000335872267204118', 'emailAddress': 'chagin.deniskpc772020@gmail.com'}, 'capabilities': {'canCopy': False, 'canEdit': True}, 'editable': True, 'copyable': False, 'writersCanShare': True, 'shared': False, 'explicitlyTrashed': False, 'appDataContents': False, 'spaces': ['drive']})


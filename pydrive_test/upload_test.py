from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title':'Test2.txt',
        "parents": [{"kind": "drive#fileLink","id": '1VYhVqDrEJJ8wos0AZQOtfnH20nXERfC4'}]})# Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Success!')  # Set content of the file from given string.
file1.Upload()

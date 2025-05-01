import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import date
import datetime

currentdate = date.today()
currenttime = datetime.datetime.now()


# Path to the service account credentials JSON file
credentials_path = 'ARK/service_account_credentials.json'

# Path to store downloaded files
download_folder = 'ARK/PODFILE'

# Authenticate using the service account credentials
# Authenticate using the service account credentials
credentials = service_account.Credentials.from_service_account_file(credentials_path)
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/drive'])

# Create a Drive API client
drive_service = build('drive', 'v3', credentials=scoped_credentials)

# ID of the folder from which to download files
folder_id = '1-KlxzTKxn9JwG9iR2leaYF-DkbYLhcT4'

# Retrieve a list of files in the folder
results = drive_service.files().list(q=f"'{folder_id}' in parents", fields='files(id, name, mimeType)').execute()
files = results.get('files', [])

# Create the download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)


conn = Dispatch_connection()
File_Cursor = conn.cursor()

# Download and delete each JPG file from the folder
for file in files:
    file_id = file['id']
    file_name = file['name']
    file_extension = os.path.splitext(file_name)[1].lower()
    file_path = os.path.join(download_folder, file_name)

    if file_extension == '.jpg':
        # Download the file
        request = drive_service.files().get_media(fileId=file_id)
        with open(file_path, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Downloading file: {file_name} - {int(status.progress() * 100)}%")

                #Insert in database
                
            # Delete the file
        drive_service.files().delete(fileId=file_id).execute()
        print(f"Deleted file: {file_name}")

print("Download completed!")
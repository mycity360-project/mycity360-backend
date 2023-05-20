from __future__ import print_function

import os.path
import base64
import json
import traceback

from google.auth.transport.requests import Request
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

# from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials

from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload

from email.mime.text import MIMEText

# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from .. import constants
from django.conf import settings
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from rest_framework.exceptions import ValidationError


def send_mail(subject, body, to_email=()):

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    # if os.path.exists(constants.TOKEN_FILE_PATH):
    #     creds = Credentials.from_authorized_user_file(
    #         constants.TOKEN_FILE_PATH, SCOPES
    #     )
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             constants.CREDENTIALS_FILE_PATH, SCOPES
    #         )
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open(constants.TOKEN_FILE_PATH, "w") as token:
    #         token.write(creds.to_json())
    # # flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    # # creds = flow.run_local_server(port=0)
    #
    # service = build("gmail", "v1", credentials=creds)
    # message = MIMEText(body)
    # message["to"] = to_email
    # message["subject"] = subject
    # create_message = {
    #     "raw": base64.urlsafe_b64encode(message.as_bytes()).decode()
    # }
    #
    # try:
    #     message = (
    #         service.users()
    #         .messages()
    #         .send(userId="me", body=create_message)
    #         .execute()
    #     )
    #     print(f'sent message to {message} Message Id: {message["id"]}')
    # except HTTPError as error:
    #     print(f"An error occurred: {error}")
    #     message = None


DRIVE_BASE_URL = "https://drive.google.com/uc?id={}"


def upload_basic(file):
    """Insert new file.
    Returns : Id's of the file uploaded
    """
    KEY_FILE_PATH = settings.GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE
    credentials = Credentials.from_service_account_file(
        KEY_FILE_PATH,
        scopes=["https://www.googleapis.com/auth/drive"],
    )
    try:
        # create drive api client
        service = build("drive", "v3", credentials=credentials)

        file_metadata = {"name": file.name}
        media = MediaIoBaseUpload(
            file, mimetype=f"image/{file.name.split('.')[-1]}"
        )
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        service.permissions().create(
            fileId=file.get("id"), body={"role": "reader", "type": "anyone"}
        ).execute()
        print(f'File ID: {file.get("id")}')
        return DRIVE_BASE_URL.format(file.get("id"))
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file


def upload_to_local(file):
    """Insert new file.
    Returns : Id's of the file uploaded
    """
    try:
        img_extension = os.path.splitext(file.name)[1]
        folder = constants.MEDIA_ROOT
        if not os.path.exists(folder):
            os.mkdir(folder)

        img_save_path = f"{folder}/{uuid4()}{img_extension}"
        with open(img_save_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        return img_save_path
    except:
        print(traceback.format_exc())
        raise ValidationError()



# if __name__ == '__main__':
#     upload_basic()

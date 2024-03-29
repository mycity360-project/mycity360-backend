from __future__ import print_function

import os.path
import base64
import json
import traceback

from google.auth.transport.requests import Request
from uuid import uuid4

from google.oauth2.credentials import Credentials

# from google.oauth2.service_account import Credentials

from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload

from email.mime.text import MIMEText

from google_auth_oauthlib.flow import InstalledAppFlow
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
    if os.path.exists(constants.TOKEN_FILE_PATH):
        try:
            creds = Credentials.from_authorized_user_file(
                constants.TOKEN_FILE_PATH, SCOPES
            )
        except:
            pass
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                flow = InstalledAppFlow.from_client_secrets_file(
                    constants.CREDENTIALS_FILE_PATH, SCOPES
                )
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                constants.CREDENTIALS_FILE_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(constants.TOKEN_FILE_PATH, "w") as token:
            token.write(creds.to_json())
    # flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    # creds = flow.run_local_server(port=0)

    service = build("gmail", "v1", credentials=creds)
    print(subject, body)
    message = MIMEText(body)
    message["to"] = to_email
    message["subject"] = subject
    create_message = {
        "raw": base64.urlsafe_b64encode(message.as_bytes()).decode()
    }

    try:
        message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None


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


def upload_to_local(file, folder=None):
    """Insert new file.
    Returns : Id's of the file uploaded
    """
    try:
        img_extension = os.path.splitext(file.name)[1]
        base_folder = f"{constants.MEDIA_ROOT}"
        if folder:
            base_folder = f"{constants.MEDIA_ROOT}{folder}/"
        if not os.path.exists(base_folder):
            os.mkdir(base_folder)
        file_name = f"{uuid4()}{img_extension}"
        img_save_path = f"{base_folder}{file_name}"
        with open(img_save_path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)
        path = f"{constants.SERVER_BASE_URL}{folder}/{file_name}"
        return path
    except:
        print(traceback.format_exc())
        raise ValidationError()


def delete_image(filename):
    try:
        os.remove(
            filename.replace(constants.SERVER_BASE_URL, constants.MEDIA_ROOT)
        )
    except:
        print(traceback.format_exc())


# if __name__ == '__main__':
#     upload_basic()

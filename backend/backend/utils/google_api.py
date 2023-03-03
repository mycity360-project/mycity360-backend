from __future__ import print_function

import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from .. import constants


def send_mail(subject, body, to_email=()):

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    if os.path.exists(constants.TOKEN_FILE_PATH):
        creds = Credentials.from_authorized_user_file(
            constants.TOKEN_FILE_PATH, SCOPES
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
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

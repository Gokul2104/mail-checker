"""
In this file oauth validation is done for Google
Credentials can be get from secrets here I am reading ig from file
"""

__author__ = "Gokul2104"

import os

from google_auth_oauthlib.flow import InstalledAppFlow
from config import cred_file, token_file
from google.oauth2.credentials import Credentials
from oauth.google_auth.constants import GMAIL


class GoogleAuth:
    def __init__(self, scope=GMAIL.SCOPE):
        """
        :param SCOPE: Scope to get access for the access token
        """
        self.__scope = scope

    def authorize(self):
        """
        Authorize and return credentials
        :return:
        """
        creds = None
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, self.__scope)
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                cred_file, self.__scope
            )
            creds = flow.run_local_server(port=0)
            with open(token_file, "w") as token:
                token.write(creds.to_json())
        return creds

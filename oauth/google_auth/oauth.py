"""
In this file oauth validation is done for Google
Credentials can be get from secrets here I am reading ig from file
"""


__author__ = "Gokul2104"

from google_auth_oauthlib.flow import InstalledAppFlow
import os

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
        flow = InstalledAppFlow.from_client_secrets_file(
            'cred.json', self.__scope
      )
        creds = flow.run_local_server(port=0)
        return creds


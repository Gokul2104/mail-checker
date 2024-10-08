from abc import ABC
from functools import cached_property

from googleapiclient.discovery import build

from oauth.google_auth.oauth import GoogleAuth


class Base(ABC):
    def __init__(self):
        self.__auth = GoogleAuth()
        self.__token = None

    def authorize(self):
        if not self.__token:
            self.__token = self.__auth.authorize()
        return self.__token

    @cached_property
    def _service(self):
        service = build("gmail", "v1", credentials=self.authorize())
        return service


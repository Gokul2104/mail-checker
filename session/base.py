import logging
import sqlite3
from functools import cached_property

from session.queries import create_table, insert_data


class BaseSession:
    def __init__(self, db="mail"):
        self.__db = db

    @cached_property
    def __client(self):
        return sqlite3.connect(self.__db).cursor()

    def create_table(self):
        """
        Creates the table if not exists
        :return:
        """
        return self.__client.execute(create_table)

    def insert(self, _id: str, subject: str, message: str, _from: str, _to: str, received_at: int, thread_id: str):
        """
        :param _id:
        :param name:
        :param subject:
        :param message:
        :param _from:
        :param _to:
        :param received_at:
        :param thread_id:
        :return:
        """
        insert_query = insert_data.format(_id=_id, subject=subject, message=message,
                                          _from=_from, _to=_to, received_at=received_at, thread_id=thread_id
                                          )
        return self.__client.execute(insert_query)

    def query(self, query: str):
        """
        Executes and return cursor
        :param query:
        :return:
        """
        return self.__client.execute(query)

    def __del__(self, *args, **kwargs):
        self.__client.close()

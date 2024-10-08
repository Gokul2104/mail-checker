from session.base import BaseSession
from tests import BaseTest
import os
from sqlite3 import OperationalError
from datetime import datetime


class TestSession(BaseTest):
    def test_001_create_table(self):
        if os.path.exists("test-mail"):
            os.remove("test-mail")
        session = BaseSession("test-mail")
        self.assertRaises(OperationalError, session.query, "SELECT * FROM 'mail_info'")
        session.create_table()
        self.assertIsNotNone(session.query("SELECT * FROM 'mail_info'"))

    def test_002_insert_recs(self):
        session = BaseSession("test-mail")
        _date = 'Mon, 7 Oct 2024 03:23:43 -0700 (PDT)'
        date_format = "%a, %d %b %Y %H:%M:%S %z (PDT)"
        session.insert("1", "sub", "mess", "abc", "def", int(datetime.strptime(_date, date_format).timestamp()), "t1")
        self.assertEqual(1, len(list(session.query("SELECT * FROM 'mail_info'"))))
        _date = 'Mon, 7 Oct 2024 03:23:43 -0700 (PDT)'
        date_format = "%a, %d %b %Y %H:%M:%S %z (PDT)"
        session.insert("2", "sub", "mess", "abc", "def", int(datetime.strptime(_date, date_format).timestamp()), "t1")
        self.assertEqual(2, len(list(session.query("SELECT * FROM 'mail_info'"))))
        self.assertEqual(1, len(list(session.query("SELECT DISTINCT(thread_id) FROM 'mail_info'"))))
        session.insert("3", "sub1", "mess", "abc", "def", int(datetime.strptime(_date, date_format).timestamp()), "t3")
        self.assertEqual(2, len(list(session.query("SELECT DISTINCT(thread_id) FROM 'mail_info'"))))



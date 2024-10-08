import json
from collections import defaultdict

from mail import ReadActions, WriteActions
from rule_engine.engine import RuleEngine, ActionEngine
from session.base import BaseSession
from tests import BaseTest

session = BaseSession("test-mail")
class TestRuleEngine(BaseTest):

    def test_001_check_or(self):
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = RuleEngine(json_data[0]['rule'], session)
        expected_query = """select DISTINCT(thread_id) from mail_info where _from = 'gokul' or subject like '%interview%' or received_at < """
        self.assertEqual(expected_query, engine.generate_query()[:-10])

    def test_002_check_negative_or(self):
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = RuleEngine(json_data[1]['rule'], session)
        self.assertRaises(ValueError, engine.generate_query)

    def test_003_check_not_or(self):
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = RuleEngine(json_data[2]['rule'], session)
        expected_query = """select DISTINCT(thread_id) from mail_info where _from != 'gokul' or subject not like '%interview%'"""
        self.assertEqual(expected_query, engine.generate_query())


class MockRead(ReadActions):

    def __init__(self):
        self.called = defaultdict(int)

    def get_label(self, label_id):
        self.called[self.get_label.__name__] += 1
        return label_id

    def get_message(self, message_id):
        self.called[self.get_message.__name__] += 1

    def get_messages(self):
        self.called[self.get_messages.__name__] += 1


class MockWrite(WriteActions):

    def __init__(self):
        self.called = defaultdict(int)

    def mark_as_read(self, thread_id):
        self.called[self.mark_as_read.__name__] += 1

    def mark_as_unread(self, thread_id):
        self.called[self.mark_as_unread.__name__] += 1

    def move_to_label(self, thread_id, label):
        self.called[self.move_to_label.__name__] += 1


class TestActionEngine(BaseTest):
    def test_001_mark_action(self):
        reader, writer = MockRead(), MockWrite()
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = ActionEngine(json_data[0]["action"], reader, writer)
        engine.execute([1, 2, 3])
        self.assertEqual(reader.called[reader.get_label.__name__], 1)
        self.assertEqual(writer.called[writer.mark_as_read.__name__], 1)
        self.assertEqual(writer.called[writer.move_to_label.__name__], 1)
        self.assertEqual(writer.called[writer.mark_as_unread.__name__], 0)

    def test_002_incorrect_action(self):
        reader, writer = MockRead(), MockWrite()
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = ActionEngine(json_data[1]["action"], reader, writer)
        self.assertRaises(AttributeError, engine.execute, [1, 2, 3])

    def test_003_mark_2_action(self):
        reader, writer = MockRead(), MockWrite()
        fp = open("mock/rule1.json")
        json_data = json.load(fp)
        fp.close()
        engine = ActionEngine(json_data[2]["action"], reader, writer)
        engine.execute([1, 2, 3])
        self.assertEqual(reader.called[reader.get_label.__name__], 2)
        self.assertEqual(writer.called[writer.mark_as_read.__name__], 1)
        self.assertEqual(writer.called[writer.move_to_label.__name__], 2)
        self.assertEqual(writer.called[writer.mark_as_unread.__name__], 0)


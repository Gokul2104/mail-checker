import json

from rule_engine.engine import RuleEngine
from tests import BaseTest


class TestRuleEngine(BaseTest):

    def test_001_check_or(self):
        json_data = json.load(open("mock/rule1.json"))
        engine = RuleEngine(json_data[0]['rule'])
        expected_query = """select * from mail_info where _from = 'gokul' or subject like '%interview%' or received_at < """
        self.assertEqual(expected_query, engine.generate_query()[:-10])

    def test_002_check_negative_or(self):
        json_data = json.load(open("mock/rule1.json"))
        engine = RuleEngine(json_data[1]['rule'])
        self.assertRaises(ValueError, engine.generate_query)

    def test_003_check_not_or(self):
        json_data = json.load(open("mock/rule1.json"))
        engine = RuleEngine(json_data[2]['rule'])
        expected_query = """select * from mail_info where _from != 'gokul' or subject not like '%interview%'"""
        self.assertEqual(expected_query, engine.generate_query())

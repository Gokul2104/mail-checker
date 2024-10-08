import datetime
import json
import sys
import config
from mail.gmail.read_actions import GmailReadActions
from mail.gmail.write_actions import GmailWriteActions
from rule_engine.engine import RuleEngine, ActionEngine
from session.base import BaseSession


class FactoryClass:
    @classmethod
    def get_class(cls, provider):
        if provider == 'gmail':
            return GmailReadActions(), GmailWriteActions()


def email_puller():
    """
    This function pulls the email and save it to database
    :return:
    """
    session = BaseSession()
    reader = GmailReadActions()
    data = reader.get_messages()
    for message in data:
        subject = None
        _from = None
        _to = None
        date = int(message['internalDate'])
        snippet = message['snippet']
        thread_id = message['threadId']
        for headers in message['payload']['headers']:
            if headers['name'] == 'Subject':
                subject = headers['value']
            if headers['name'] == 'From':
                _from = headers['value']
            if headers['name'] == 'To':
                _to = headers['value']

        session.create_table()
        session.insert(_id=message['id'], subject=subject, message=snippet, _from=_from, _to=_to, received_at=date,
                       thread_id=thread_id)
        session.commit()


def execute_actions():
    session = BaseSession()
    fp = open(config.rule_path)
    rules = json.load(fp)
    fp.close()
    for rule in rules:
        rule_engine = RuleEngine(rule["rule"], session)
        thread_ids = rule_engine.execute()
        reader, writer = FactoryClass.get_class("gmail")
        action_engine = ActionEngine(rule["action"], reader, writer)
        print(thread_ids)
        action_engine.execute(thread_ids)
        print(f"Applied Rule {rule['rule']}")


if __name__ == '__main__':
    if sys.argv[1] == "pull":
        email_puller()
    if sys.argv[1] == "rule":
        execute_actions()



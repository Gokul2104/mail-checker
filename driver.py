from mail import GmailReadActions
from rule_engine.engine import RuleEngine
from session.base import BaseSession


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


def execute_actions(rules):
    session = BaseSession()
    for rule in rules:
        rule_engine = RuleEngine(rule["rule"], session)
        thread_ids = rule_engine.execute()
        print(thread_ids)


if __name__ == '__main__':
    email_puller()

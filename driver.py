from mail import GmailReadActions
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


if __name__ == '__main__':
    email_puller()

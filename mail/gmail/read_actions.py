import logging

from googleapiclient.errors import HttpError

from mail.read_actions import ReadActions
from mail.gmail.base import Base


class GmailReadActions(ReadActions, Base):

    def get_label(self, label_name):
        """
        get all the labels
        :return:
        """
        next_token = True
        label_id = None
        while next_token:
            next_token = None if next_token is True else next_token
            labels = self._service.users().labels().list(userId="me").execute()
            for label in labels['labels']:
                if label['name'] == label_name:
                    return label['id']
            next_token = labels.get("nextPageToken")
        return None



    def get_message(self, message_id):
        """
        Return details of current message
        :param message_id:
        :return:
        """
        return self._service.users().messages().get(userId="me", id=message_id).execute()

    def get_messages(self):
        """
        return all emails from gmail
        :return:
        """
        # limiting to default limit of 10 email for this purpose
        message = self._service.users().messages().list(userId="me", maxResults=50).execute()
        for data in message["messages"]:
            yield self.get_message(data['id'])






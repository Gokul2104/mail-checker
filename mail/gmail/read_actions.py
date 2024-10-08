from mail.read_actions import ReadActions
from mail.gmail.base import Base


class GmailReadActions(ReadActions, Base):

    def get_label(self, label_id):
        """
        get all the labels
        :return:
        """
        data = self._service

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
        message = self._service.users().messages().list(userId="me", maxResults=10).execute()
        for data in message["messages"]:
            yield self.get_message(data['id'])






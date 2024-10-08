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
        pass

    def get_messages(self):
        """
        return all emails from gmail
        :return:
        """
        pass

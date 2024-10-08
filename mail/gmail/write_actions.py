from mail import WriteActions
from mail.read_actions import ReadActions
from mail.gmail.base import Base


class GmailWriteActions(WriteActions, Base):
    def mark_as_read(self, thread_ids):
        """
        Mark threads as read
        :param thread_ids:
        :return:
        """
        pass

    def mark_as_unread(self, thread_ids):
        """
        Mark threads as unread
        :param thread_ids:
        :return:
        """
        pass

    def move_to_label(self, thread_ids, label):
        """
        move threads to unread
        :param thread_ids:
        :param label:
        :return:
        """
        pass

from mail import WriteActions
from mail.gmail.base import Base


class GmailWriteActions(WriteActions, Base):
    def mark_as_read(self, thread_ids):
        """
        Mark threads as read
        :param thread_ids:
        :return:
        """
        batch = self._service.new_batch_http_request()
        for thread_id in thread_ids:
            batch.add(self._service.users().threads().modify(userId='me', id=thread_id, body={'removeLabelIds': ['UNREAD']}))
        batch.execute()

    def mark_as_unread(self, thread_ids):
        """
        Mark threads as unread
        :param thread_ids:
        :return:
        """
        batch = self._service.new_batch_http_request()
        for thread_id in thread_ids:
            batch.add(self._service.users().threads().modify(userId='me', id=thread_id, body={'addLabelIds': ['UNREAD']}))
        batch.execute()

    def move_to_label(self, thread_ids, label):
        """
        move threads to unread
        :param thread_ids:
        :param label:
        :return:
        """
        batch = self._service.new_batch_http_request()
        for thread_id in thread_ids:
            batch.add(self._service.users().threads().modify(userId='me', id=thread_id, body={'addLabelIds': [label]}))
        batch.execute()

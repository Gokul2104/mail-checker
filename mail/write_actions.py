from abc import ABC, abstractmethod

from mail.base_actions import BaseAction


class WriteActions(BaseAction, ABC):

    @abstractmethod
    def mark_as_read(self, thread_id):
        raise NotImplementedError()

    @abstractmethod
    def mark_as_unread(self, thread_id):
        raise NotImplementedError()

    @abstractmethod
    def move_to_label(self, thread_id, label):
        raise NotImplementedError()




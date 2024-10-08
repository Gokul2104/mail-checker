from abc import ABC, abstractmethod

from mail.base_actions import BaseAction


class ReadActions(BaseAction, ABC):
    @abstractmethod
    def get_label(self, label_id):
        raise NotImplementedError()

    @abstractmethod
    def get_message(self, message_id):
        raise NotImplementedError()

    @abstractmethod
    def get_messages(self):
        raise NotImplementedError()

from abc import ABC

from mail.BaseActions import BaseAction


class ReadActions(ABC, BaseAction):
    def get_labels(self):
        pass

    def get_message(self, q):
        pass

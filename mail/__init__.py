from mail.base_actions import BaseAction
from mail.gmail.read_actions import GmailReadActions
from mail.read_actions import ReadActions
from mail.write_actions import WriteActions


class FactoryClass:
    @classmethod
    def get_class(cls, provider):
        if provider == 'gmail':
            return GmailReadActions(),

from abc import ABC

from mail import WriteActions
from rule_engine.base_field import BaseField
from rule_engine.constants import MarkActionConstant


class ActionField(BaseField, ABC):

    def __init__(self, data, provider):
        super().__init__(data)
        self.__provider: WriteActions = provider

    @property
    def to(self):
        return self._data["To"]


class MarkAction(ActionField):
    def _validate(self):
        if self.to not in MarkActionConstant.ALLOWED_TO:
            raise ValueError("Action Not supported")


class MoveAction(ActionField):
    def _validate(self):
        if self.to not in self.__provider.get_labels():
            raise ValueError("mentioned label not found")

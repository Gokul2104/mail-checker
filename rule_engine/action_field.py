from abc import ABC, abstractmethod

from mail import WriteActions, ReadActions
from rule_engine.base_field import BaseField
from rule_engine.constants import MarkActionConstant


class ActionField(BaseField, ABC):

    def __init__(self, data, reader: ReadActions, writer: WriteActions):
        super().__init__(data)
        self._r_provider = reader
        self._w_provider = writer

    @property
    def to(self):
        return self._data["To"]

    @abstractmethod
    def _act(self, thread_ids: list):
        raise NotImplementedError()

    def execute(self, thread_ids: list):
        self._validate()
        self._act(thread_ids)


class MarkAction(ActionField):
    def _validate(self):
        if self.to not in MarkActionConstant.ALLOWED_TO:
            raise ValueError("Action Not supported")

    def _act(self, thread_ids: list):
        if self.to == MarkActionConstant.READ:
            self._w_provider.mark_as_read(thread_ids)
        else:
            self._w_provider.mark_as_unread(thread_ids)


class MoveAction(ActionField):
    def __init__(self, data, reader: ReadActions, writer: WriteActions):
        super().__init__(data, reader, writer)
        self.__label_id = None

    def _validate(self):
        self.__label_id = self._r_provider.get_label(self.to)
        if not self.__label_id:
            raise ValueError("mentioned label not found")

    def _act(self, thread_ids: list):
        print(self.__label_id)
        self._w_provider.move_to_label(thread_ids, self.__label_id)

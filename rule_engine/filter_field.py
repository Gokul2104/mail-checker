from abc import ABC, abstractmethod

from rule_engine.base_field import BaseField


class FilterField(ABC, BaseField):
    @property
    def value(self):
        return self.data["Value"]

    @property
    def predicate(self):
        return self.data["Predicate"]

    @property
    def field(self):
        return self.data["Field"]

    @abstractmethod
    def generate_filter(self):
        raise NotImplemented()


class StringField(FilterField):
    pass


class DateTimeField(FilterField):
    pass


class From(StringField):
    pass


class To(StringField):
    pass


class Subject(StringField):
    pass


class Message(StringField):
    pass


class ReceivedAt(DateTimeField):
    pass

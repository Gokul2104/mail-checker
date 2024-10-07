from abc import ABC


class BaseField(ABC):
    def __init__(self, data):
        self.data = data

    def validate(self):
        raise NotImplemented()

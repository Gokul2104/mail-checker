from abc import ABC


class BaseField(ABC):
    def __init__(self, data):
        self._data = data

    def _validate(self):
        raise NotImplemented()

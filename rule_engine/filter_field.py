from abc import ABC, abstractmethod

from rule_engine.base_field import BaseField
from rule_engine.constants import StringFieldConstant, DateTimeFieldConstant
from session.queries import Columns
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz


class FilterField(BaseField, ABC):
    db_field = Columns.FROM

    @property
    def value(self):
        return self._data["Value"]

    @property
    def predicate(self):
        return self._data["Predicate"]

    @property
    def field(self):
        return self._data["Field"]

    @abstractmethod
    def _generate_filter(self):
        raise NotImplementedError()

    def execute(self):
        self._validate()
        return self._generate_filter()


class StringField(FilterField):
    def _validate(self):
        """
        Validate all rules for string field
        :return:
        """
        if self.predicate not in StringFieldConstant.ALLOWED_PREDICATE:
            raise ValueError(f"Predicate should be one off {StringFieldConstant.ALLOWED_PREDICATE}")
        if not isinstance(self.value, str):
            raise ValueError("Value Should be of type str")

    def _generate_filter(self):
        """
        Create the filter for operators
        :return:
        """
        ops = StringFieldConstant.OPERATOR_MAP[self.predicate]
        value = f"%{self.value}%" if ops in ("like", "not like") else self.value
        db_data = f"{self.db_field} {ops} '{value}'"
        return db_data


class DateTimeField(FilterField):
    @property
    def metrics(self):
        return self._data["Metrics"]

    def _validate(self):
        if self.predicate not in DateTimeFieldConstant.ALLOWED_PREDICATE:
            raise ValueError(f"Predicate should be one off {DateTimeFieldConstant.ALLOWED_PREDICATE}")
        if not isinstance(self.value, int):
            raise ValueError("Value Should be of type int")
        if self.metrics in DateTimeFieldConstant.ALLOWED_UNIT:
            raise ValueError(f"Unit should be one of {DateTimeFieldConstant.ALLOWED_UNIT}")

    def _generate_filter(self):
        ops = DateTimeFieldConstant.OPERATOR_MAP[self.predicate]
        timezone = pytz.timezone('UTC')
        rel = {"day": self.value} if self.metrics == "day" else {"month": self.value}
        st_dt = datetime.now(timezone) - relativedelta(**rel)
        value = int(st_dt.timestamp())
        db_data = f"{self.db_field} {ops} {value}"
        return db_data


class FromField(StringField):
    db_field = Columns.FROM


class ToField(StringField):
    db_field = Columns.TO


class SubjectField(StringField):
    db_field = Columns.SUBJECT


class MessageField(StringField):
    db_field = Columns.MESSAGE


class ReceivedAtField(DateTimeField):
    db_field = Columns.RECEIVED_AT

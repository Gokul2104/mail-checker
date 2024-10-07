from rule_engine.filter_field import FromField, ToField, SubjectField, MessageField, ReceivedAtField, FilterField
from session.base import BaseSession

field_map = {
    "From": FromField,
    "To": ToField,
    "Subject": SubjectField,
    "Message": MessageField,
    "Received At": ReceivedAtField
}


class RuleEngine:
    def __init__(self, rule):
        self.__rule = rule
        self.__session = BaseSession()

    @property
    def apply(self):
        return self.__rule["apply"]

    @property
    def filter(self):
        return self.__rule["filter"]

    def generate_query(self):
        """
        Whole query generation logic lies here
        :return:
        """
        cond = " and " if self.apply == "all" else " or "
        base_query = "select * from mail_info where "
        for curr_filter in self.filter:
            field_cls = field_map.get(curr_filter["Field"], None)
            if not field_cls:
                raise AttributeError(f"Unsupported Field f{curr_filter['Field']}")
            base_query += field_cls(curr_filter).execute() + cond
        base_query = base_query.rsplit(cond, 1)[0]
        return base_query

    def execute(self):
        return self.__session.query(self.generate_query())


class ActionEngine:
    pass

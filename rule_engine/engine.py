from mail import ReadActions, WriteActions
from rule_engine.action_field import MarkAction, MoveAction
from rule_engine.filter_field import FromField, ToField, SubjectField, MessageField, ReceivedAtField, FilterField
from session.base import BaseSession

field_map = {
    "From": FromField,
    "To": ToField,
    "Subject": SubjectField,
    "Message": MessageField,
    "Received At": ReceivedAtField
}
action_map = {
    "mark": MarkAction,
    "move": MoveAction
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
        base_query = "select DISTINCT(thread_id) from mail_info where "
        for curr_filter in self.filter:
            field_cls = field_map.get(curr_filter["Field"], None)
            if not field_cls:
                raise AttributeError(f"Unsupported Field f{curr_filter['Field']}")
            base_query += field_cls(curr_filter).execute() + cond
        base_query = base_query.rsplit(cond, 1)[0]
        return base_query

    def execute(self):
        """
        Return all the thread ids of the current matching message
        if we need to use between thread,message ids update here as well as the query
        :return:
        """
        data = self.__session.query(self.generate_query())
        thread_ids = [i[0] for i in data]
        return thread_ids


class ActionEngine:
    def __init__(self, actions: list, r_provider: ReadActions, w_provider: WriteActions):
        self.__actions = actions
        self.__w_provider = w_provider
        self.__r_provider = r_provider

    def execute(self, thread_ids):
        for action in self.__actions:
            action_cls = action_map.get(action["Type"], None)
            if not action_cls:
                raise AttributeError(f"Unsupported action f{action['Type']}")
            action_cls(action, reader=self.__r_provider, writer=self.__w_provider).execute(thread_ids)

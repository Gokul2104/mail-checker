class StringFieldConstant:
    ALLOWED_FIELDS = ("From", "To", "Subject", "Message")
    ALLOWED_PREDICATE = ("contains", "not contains", "equals", "does not equals")
    OPERATOR_MAP = {
        "contains": "like",
        "not contains": "not like",
        "equals": "=",
        "does not equals": "!="
    }


class DateTimeFieldConstant:
    ALLOWED_FIELDS = ("Received At",)
    ALLOWED_PREDICATE = ("less than", "greater than")
    ALLOWED_UNIT = ("month", "day")
    OPERATOR_MAP = {
        "less than": "<",
        "greater than": ">"
    }


class MarkActionConstant:
    READ = "read"
    UNREAD = "unread"
    ALLOWED_TO = (READ, UNREAD)



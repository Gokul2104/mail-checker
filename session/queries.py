class Columns:
    ID = "_id"
    SUBJECT = "subject"
    MESSAGE = "message"
    FROM = "_from"
    TO = "_to"
    RECEIVED_AT = "received_at"
    THREAD_ID = "thread_id"


create_table = """CREATE TABLE IF NOT EXISTS mail_info (
    "_id" TEXT PRIMARY KEY,
    "subject" TEXT,
    "thread_id" TEXT,
    "message" TEXT,
    "_from" TEXT,
    "_to" TEXT,
    "received_at" INTEGER
);
"""

insert_data = """
insert into mail_info (_id, subject, message, _from, _to, received_at, thread_id) values (?,?,?,?,?,?,?);
"""

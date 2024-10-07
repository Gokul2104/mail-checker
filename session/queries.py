create_table = """CREATE TABLE IF NOT EXISTS mail_info (
    "_id" TEXT PRIMARY KEY,
    "subject" TEXT,
    "message" TEXT,
    "_from" TEXT,
    "_to" TEXT,
    "received_at" INTEGER
);
"""
insert_data = """
insert into mail_info (_id, subject, message, _from, _to, received_at) values
 ("{_id}", "{subject}", "{message}", "{_from}", "{_to}", {received_at});
"""

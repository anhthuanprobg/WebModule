# mongodb://<dbuser>:<dbpassword>@ds247171.mlab.com:47171/ct4-movie

import mongoengine

host = "ds247171.mlab.com"
port = 47171
db_name = "ct4-movie"
user_name = "admin"
password = "codethechange18"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
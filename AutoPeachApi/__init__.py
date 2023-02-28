import uuid

from tinydb import TinyDB, Query, where

db = TinyDB('db.json')
Q = Query()


def register_cron():
    return None


class Cron:
    @classmethod
    def register(cls):
        pass


class Storage:
    def __init__(self, block):
        self.block = block

    def get_all(self):
        p = db.table(self.block).all()
        return p

    def save(self, data):
        if '_id' in data:
            db.table(self.block).update(data, where('_id') == data['_id'])
        else:
            data['_id'] = str(uuid.uuid1())
            db.table(self.block).insert(data)

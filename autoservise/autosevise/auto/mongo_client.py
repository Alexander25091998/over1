# pip install pymongo
from pymongo import MongoClient


class MongoCl:
    def __init__(self, connection_url, db_name):
        self.connection_url = connection_url
        self.db_name = db_name

    def _get_db_client(self):
        return MongoClient(self.connection_url)[self.db_name]

    def get_collection(self, collection_name):
        db_client = self._get_db_client()
        return db_client[collection_name].find()
        # return db_client[collection_name].find().sort({"age": -1})

    def insert(self, collection_name, items):
        db_client = self._get_db_client()
        db_client[collection_name].insert_many(items)

    def find_all(self, collection_name, filed_name, field_value):
        db_client = self._get_db_client()
        return db_client[collection_name] \
            .find({filed_name: field_value})

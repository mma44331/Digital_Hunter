import os

from pymongo import MongoClient


class MongoDB:
    def __init__(self, logger):
        self.logger = logger
        self.my_client = MongoClient(os.getenv('MONGO_URI'))
        self.my_db = self.my_client['target_bank']
        self.my_col = self.my_db['targets']
        self.conn = self._connect_mongo()


    def _connect_mongo(self):
        return self.my_col

    def get_by_target_id(self,id):
        target = self.conn.find({'signal_id':id},{})
        if target:
            return target
        return  None
    def insert_one(self, message):
        self.conn.update_one({'signal_id':message['signal_id']},{'$set':message},upsert=True)

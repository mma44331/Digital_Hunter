
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

    #
    def update(self, message):
        try:
            self.conn.update_many({'attack_id':message['attack_id']},{'$set':{'result':message['result']}},upsert=True)
        except Exception as e:
            self.logger('error',e)

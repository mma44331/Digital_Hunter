import os


class Config:
    def __init__(self):
        self.bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS','kafka:9092')
        self.topic_attack = os.getenv('TOPIC_ATTACK','attack')
        self.db_name = os.getenv('DB_NAME','target_bank')
        self.coll_name = os.getenv('COLL_NAME','targets')


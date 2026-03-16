import os


class Config:
    def __init__(self):
        self.bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS','kafka:9092')
        self.topic_intel = os.getenv('TOPIC_INTEL','intel')
        self.topic_intel_signals_dlq = os.getenv('TOPIC_INTEL_SIGNALS_DLQ','intel_signals_dlq')
        self.db_name = os.getenv('DB_NAME','target_bank')
        self.coll_name = os.getenv('COLL_NAME','targets')


from config import Config
from consumer import KafkaConsumer
from mongo_db import MongoDB
from shards.logger import log_event as logger

config = Config()
mongo_db = MongoDB(logger)
consumer = KafkaConsumer(logger,config.bootstrap_servers,config.topic_attack,mongo_db)


if __name__ == "__main__":
    consumer.start_attack()
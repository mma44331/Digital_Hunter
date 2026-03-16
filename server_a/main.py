from config import Config
from consumer import KafkaConsumer
from mongo_db import MongoDB
from validations import Validation
from simulator import run_simulator
from shards.logger import log_event as logger

config = Config()
mongo_db = MongoDB(logger)
validate = Validation(logger,config.bootstrap_server,config.topic_intel_signals_dlq,mongo_db)
consumer = KafkaConsumer(logger,config.bootstrap_server,config.topic_intel,validate,mongo_db)


if __name__ == "__main__":
    run_simulator()
    consumer.start_intel()
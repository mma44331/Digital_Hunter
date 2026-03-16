import json

from confluent_kafka import Consumer

class KafkaConsumer:
    def __init__(self, logger,bootstrap_servers,topic_name,mongo_db):
        self.logger = logger
        self.mongo_db = mongo_db
        self.consumer = Consumer({'bootstrap.servers':bootstrap_servers,
                                  'group.id':'service_b',
                                  'auto.offset.reset':'earliest'})
        self.topic_name = topic_name


    def start_attack(self):
        self.consumer.subscribe([self.topic_name])
        self.logger('info','subscribed to topic attack')
        while True:
            try:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    self.logger('info', 'There are currently no messages in the attack topic')
                    continue

                message = msg.value().decode('utf-8')
                message = json.loads(message)
                self.mongo_db.update(message)
                self.logger('info','Sending success to Mongo')
            except Exception as e:
                self.logger('error', str(e))






import json

from confluent_kafka import Consumer

class KafkaConsumer:
    def __init__(self, logger,bootstrap_servers,topic_name,validate,mongo_db):
        self.logger = logger
        self.mongo_db = mongo_db
        self.validate = validate
        self.consumer = Consumer({'bootstrap.servers':bootstrap_servers,
                                  'group.id':'service_a',
                                  'auto.offset.reset':'earliest'})
        self.topic_name = topic_name


    def start_intel(self):
        self.consumer.subscribe([self.topic_name])
        self.logger('info','subscribed to topic intel')
        while True:
            try:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    self.logger('info', 'There are currently no messages in the intel topic')
                    continue
                if msg.error():
                    self.logger('error','message error')


                message = msg.value().decode('utf-8')
                message = json.loads(message)
                flage = self.validate.validate_fields(message)
                if not flage:
                    continue
                message = self.validate.crucifixion(message)
                message = self.validate.distance_comparison(message)
                self.mongo_db.insert_one(message)
                self.logger('info','Sending success to Mongo')
            except Exception as e:
                self.logger('error', str(e))






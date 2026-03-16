from confluent_kafka import Consumer

class KafkaConcumer:
    def __init__(self, logger,bootstrap_server,topic_intel,topic_attack,topic_damage):
        self.logger = logger
        self.consumer = Consumer({'bootstrap.server':bootstrap_server,
                                  'group_id':'all_topics',
                                  'auto.offset.reset':'earliest'})
        self.topic_intel = topic_intel
        self.topic_attack = topic_attack
        self.topic_damage = topic_damage

    def start_intel(self):
        self.consumer.subscribe([self.topic_intel])
        self.logger('info','subscribed to topic intel')
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                self.logger('info', 'There are currently no messages in the intel topic')
                continue




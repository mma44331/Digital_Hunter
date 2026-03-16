import json
from haversine import haversine_km
from confluent_kafka import Producer

class Validation:
    def __init__(self,logger,bootstrap_server,topic,mongo_db):
        self.logger = logger
        self.topic = topic
        self.mongo_db = mongo_db
        self.producer = Producer({'bootstrap.server': bootstrap_server})

    def validate_fields(self, message):
        if message['signal_id'] is None or message['entity_id'] is None or message['reported_lat'] is None or message['reported_lon'] is None:
            message['error'] = 'missing critical fields'
            json_data = json.dumps(message, default=str).encode('utf-8')
            self.producer.produce(self.topic,json_data)
            self.producer.flush()
            self.logger('error','missing critical fields')
            return False
        return True

    def crucifixion(self, message):
        target = self.mongo_db.get_by_target_id(message['signal_id'])
        if target is None:
            message['priority_level'] = 99
        return message

    def distance_comparison(self,message):
        target = self.mongo_db.get_by_target_id(message['signal_id'])
        distance = 0
        if target:
            lat = target['lon']
            lon = target['lon']
            distance = haversine_km(lat,lon,message['lat'],message['lon'])
        message['distance'] = distance
        return message


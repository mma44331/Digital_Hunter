import os


class Config:
    def __init__(self):
        self.bootstrap_server = os.getenv('BOOTSTRAP_SERVER','kafka:9092')
        self.topic_intel = os.getenv('TOPIC_INTEL','intel')
        self.topic_attack = os.getenv('TOPIC_ATTACK','attack')
        self.topic_damage = os.getenv('TOPIC_DAMAGE','damage')
        self.topic_intel_signals_dlq = os.getenv('INTEL_SIGNALS_DLQ','intel_signals_dlq')



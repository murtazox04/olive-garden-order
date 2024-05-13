from confluent_kafka import Producer
from decouple import config

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
    # 'security.protocol': config("KAFKA_SECURITY_PROTOCOL"),
    # 'sasl.username': config("KAFKA_SASL_USERNAME"),
    # 'sasl.password': config("KAFKA_SASL_PASSWORD"),
    # 'sasl.mechanism': config("KAFKA_SASL_MECHANISM"),
    # 'group.id': 'myGroup',
    # 'auto.offset.reset': 'earliest'
})

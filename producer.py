# Producer file that initializes and sends JSON data to a Kafka service

from helpers.util import get_UTC_time, get_host_name
from helpers.init_kafka import initialize_kafka_producer

producer = initialize_kafka_producer()
producer.send(
    "sample_topic", {"utc_time": get_UTC_time(), "host_name": get_host_name()}
)
producer.flush()  # For send messages

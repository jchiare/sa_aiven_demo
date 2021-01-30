# Producer file that initializes and sends JSON data to a Kafka service

from kafka import KafkaProducer
import json
from helpers import get_UTC_time, get_host_name

producer = KafkaProducer(
    bootstrap_servers="server-name:port",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

producer.send(
    "sample_topic", {"utc_time": get_UTC_time(), "host_name": get_host_name()}
)

# Force sending of all messages

producer.flush()  # block

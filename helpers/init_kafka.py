# Helper file to initialize Kafka producer

"""
Adapted from kafka_helpers.py https://github.com/gfrolov/aiven-kafka/blob/master/kafka_helpers.py
"""

from kafka import KafkaProducer
from json import dumps
from os import environ


def get_kafka_broker():
    """
    Parses the KAKFA_URL and returns a hostname: port that kafka - python expects.
    Expects to be stored in environ var as "brokername,port"
    """
    if not environ.get("KAFKA_URL"):
        raise RuntimeError("The KAFKA_URL config variable is not set.")

    kafka_url = environ.get("KAFKA_URL").split(",")
    return "{}:{}".format(kafka_url[0], kafka_url[1])


def get_kafka_ssl_info():
    """
    Expects the following variables to be set KAFKA_CA, KAFKA_SERVICE_CERT, KAFKA_SERVICE_KEY
    to file locations of each of the corresponding files
    KAFKA_CA - ca.pem
    KAFKA_SERVICE_CERT - service.cert
    KAFKA_SERVICE_KEY - service.key
    """

    if not environ.get("KAFKA_CA"):
        raise RuntimeError("The KAFKA_CA config variable is not set.")
    if not environ.get("KAFKA_SERVICE_CERT"):
        raise RuntimeError("The KAFKA_SERVICE_CERT config variable is not set.")
    if not environ.get("KAFKA_SERVICE_KEY"):
        raise RuntimeError("The KAFKA_SERVICE_KEY config variable is not set.")

    ssl_info = {}
    ssl_info["ssl_cafile"] = environ["KAFKA_CA"]
    ssl_info["ssl_certfile"] = environ["KAFKA_SERVICE_CERT"]
    ssl_info["ssl_keyfile"] = environ["KAFKA_SERVICE_KEY"]

    return ssl_info


def initialize_kafka_producer():
    """
    Return a KafkaProducer that uses the configured Kafka broker and corresponding SSL info
    """
    ssl_info = get_kafka_ssl_info()

    producer = KafkaProducer(
        bootstrap_servers=get_kafka_broker(),
        security_protocol="SSL",
        ssl_cafile=ssl_info["ssl_cafile"],
        ssl_certfile=ssl_info["ssl_certfile"],
        ssl_keyfile=ssl_info["ssl_keyfile"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )

    return producer

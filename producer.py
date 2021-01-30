# Producer file that initializes and sends JSON data to a Kafka service

from helpers.util import get_UTC_time, get_host_name
from helpers.init_kafka import initialize_kafka_producer
from argparse import ArgumentParser
from typing import Text


def kafka_producer_service(topic_name: Text):
    producer = initialize_kafka_producer()

    message_key = get_host_name()
    message_value = {"UTC_time": get_UTC_time()}

    producer.send(topic_name, value=message_value, key=message_key)
    producer.flush()  # Send messages


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--topic", help="Kafka topic name", required=True)
    args = parser.parse_args()

    kafka_producer_service(args.topic)


if __name__ == "__main__":
    main()

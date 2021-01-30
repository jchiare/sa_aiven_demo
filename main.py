from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-t', '--topic',
                        help="Kafka topic name",
                        required=True)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
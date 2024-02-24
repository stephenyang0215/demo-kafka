from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
client_config = dict(config_parser['kafka_client'])

ice_producer = Producer(client_config)
topping_consumer = Consumer(client_config)
topping_consumer.subscribe(['topping'])

def run():
    while True:
        record = topping_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            add_ice(record.key(), boba)


def add_ice(order_id, boba):
    if boba.ice == "0":
        print("No Ice")
    else :
        print(f"Add {boba.ice}% Ice!")
    ice_producer.produce("ice", key=order_id, value=json.dumps(boba))

if __name__ == '__main__':
    run()


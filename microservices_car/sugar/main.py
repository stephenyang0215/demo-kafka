from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
client_config = dict(config_parser['kafka_client'])

sugar_producer = Producer(client_config)
milk_consumer = Consumer(client_config)
milk_consumer.subscribe(['milk'])

def run():
    while True:
        record = milk_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            add_sugar(record.key(), boba)

def add_sugar(order_id, boba):
    if boba.sugar == "0":
        print("Sugar Free!")
        boba.price-=0.5 # Health promotion discount
    else:
        print(f"Add {boba.sugar}% sugar!")
    sugar_producer.produce("sugar", key=order_id, value=json.dumps(boba))


if __name__ == '__main__':
    run()


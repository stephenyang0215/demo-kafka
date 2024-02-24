from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
client_config = dict(config_parser['kafka_client'])

tea_producer = Producer(client_config)
order_consumer = Consumer(client_config)
order_consumer.subscribe(['orders'])

def run():
    while True:
        record = order_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            print(type(boba))
            print(boba)
            add_tea(record.key(), boba)

def add_tea(order_id, boba):
    if boba['tea'] == "Black_Tea":
        print("Add black tea!")
        boba['price'] += 1.5
    elif boba['tea'] == "White_Tea":
        print("Add white tea!")
        boba['price'] += 1
    elif boba['tea'] == "Herbal_Tea":
        print("Add herbal tea!")
        boba['price'] += 1.5
    elif boba['tea'] == "Yellow_Tea":
        print("Add yellow tea!")
        boba['price'] += 1
    tea_producer.produce("tea", key=order_id, value=json.dumps(boba))

if __name__ == '__main__':
    run()


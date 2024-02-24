from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
client_config = dict(config_parser['kafka_client'])

milk_producer = Producer(client_config)
tea_consumer = Consumer(client_config)
tea_consumer.subscribe(['tea'])

def run():
    while True:
        record = tea_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            add_milk(record.key(), boba)

def add_milk(order_id, boba):
    if boba['milk'] == "Whole_Milk":
        print("Add whole milk!")
        boba['price'] = boba['price']+1
    elif boba['milk'] == "Low-Fat_Milk":
        print("Add low fat milk!")
        boba['price'] = boba['price']+1
    elif boba['milk'] == "Oat_Milk":
        print("Add oat milk!")
        boba['price'] = boba['price']+2
    elif boba['milk'] == "Nut_Milk":
        print("Add nut milk!")
        boba['price'] = boba['price']+1.5
    milk_producer.produce("milk", key=order_id, value=json.dumps(boba))

if __name__ == '__main__':
    run()


from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
client_config = dict(config_parser['kafka_client'])

topping_producer = Producer(client_config)
sugar_consumer = Consumer(client_config)
sugar_consumer.subscribe(['sugar'])

def run():
    while True:
        record = sugar_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            add_topping(record.key(), boba)

def add_topping(order_id, boba):
    if boba.topping == "Agar_Pearls":
        print("Add agar pearls")
        boba.price+=1
    elif boba.sugar == "Coconut_Jelly":
        print("Add Coconut Jelly!")
        boba.price += 1.5
    elif boba.sugar == "Taro_Balls":
        print("Add Taro Balls!")
        boba.price += 1.5
    elif boba.sugar == "Boba":
        print("Add Boba!")
        boba.price += 1
    elif boba.sugar == "Grass_Jelly":
        print("Add Grass Jelly!")
        boba.price += 1
    topping_producer.produce("topping", key=order_id, value=json.dumps(boba))

if __name__ == '__main__':
    run()
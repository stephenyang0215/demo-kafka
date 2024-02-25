import json

from order import BobaTea, TeaOrder
from configparser import ConfigParser
from confluent_kafka import Producer, Consumer

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
producer_config = dict(config_parser['kafka_client'])
consumer_config = dict(config_parser['kafka_client'])##Try removing it
consumer_config.update(config_parser['consumer'])
boba_producer = Producer(producer_config)
order_list = {}

def place_order(count, tea, milk, sugar, topping, ice):
    count = int(count)
    sugar = int(sugar)
    ice = int(ice)
    order = TeaOrder(count)
    order_list[order.id] = order
    for i in range(count):
        boba_tea = BobaTea(tea, milk, sugar, topping, ice)
        boba_tea.order_id = order.id
        boba_producer.produce('orders', key=order.id, value = boba_tea.to_json())
    boba_producer.flush()
    return order.id

def get_order(order_id):
    order = order_list[order_id]
    if order == None:
        return "Order not exists."
    else:
        return order.to_json()

def load_orders():
    boba_consumer = Consumer(consumer_config)
    boba_consumer.subscribe(['ice'])
    while True:
        record = boba_consumer.poll(0.1)
        if record is None:
            pass
        elif record.error():
            pass
        else:
            boba = json.loads(record.value())
            add_bobatea(record.key(), boba)

def add_bobatea(order_id, boba):
    if order_id in order_list.keys():
        order = order_list[order_id]
        order.add_boba(boba)

if __name__ == '__main__':
    order_id = place_order(1, 'Black_Tea', 'Oat_Milk', 10, 'Taro_Balls', 10)

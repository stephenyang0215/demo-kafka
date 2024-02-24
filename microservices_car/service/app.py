from flask import Flask
from threading import Thread
import json
import service

app = Flask(__name__)

@app.route('/order/<count>/<tea>/<milk>/<sugar>/<topping>/<ice>', methods=['POST'])
def order_pizzas(count, tea, milk, sugar, topping, ice):
    order_id = service.place_order(count, tea, milk, sugar, topping, ice)
    return json.dumps({'order_id': order_id})
#1/Black_Tea/Whole_Milk/10/Taro_Balls/10

@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    return service.get_order(order_id)

if __name__ == "__main__":
    app.run(debug=True)

@app.before_first_request
def launch_consumer():
    t = Thread(target=service.load_orders)
    t.start()

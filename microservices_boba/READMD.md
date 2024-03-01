This is the practice of kafka microservice architecture.
The subject is to manage the operation of boba tea shop. 
Once the shop receives the order, it will trigger the API call detailing the specification for the drinks.
It consists of five steps of processing the operation:
1. tea
2. sugar
3. milk
4. topping
5. ice

In this case, I use Flask framework to build the APIs for the app,
which allow client to specify the drink components as parameters for each step.

(POST)\
count: number of drinks\
tea: type of tea\
milk: amount of milk\
sugar: amount of sugar\
topping: type of topping\
ice: amount of ice
localhost:8000/order/<count<f>>/<tea<f>>/<milk<f>>/<sugar<f>>/<topping<f>>/<ice<f>>
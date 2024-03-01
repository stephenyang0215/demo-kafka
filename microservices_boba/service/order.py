import json
import uuid
class BobaTea:
    def __init__(self, tea, milk, sugar, topping, ice):
        self.order_id = ''
        self.tea = tea
        self.milk = milk
        self.sugar = sugar
        self.topping = topping
        self.ice = ice
        self.price = 0

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    def __str__(self):
        return json.dumps(self.__dict__)

class TeaOrder:
    def __init__(self, count):
        self.id = str(uuid.uuid4().int)
        self.count = count
        self.boba_tea = []

    def add_boba(self, boba):
            self.boba_tea.append(boba)

    def get_boba_tea(self):
        return self.boba_tea

    def __str__(self):
        return json.dumps(self.__dict__)

    def to_json(self):
        return json.dumps(self, default=lambda o:o.__dict__,
                          sort_keys=False, indent=4)

    def add_boba(self, boba):
        self.boba_tea.append(boba)


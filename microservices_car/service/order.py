import json
import uuid
class BobaTea:
    def __init__(self):
        self.order_id
        self.tea
        self.milk
        self.sugar
        self.topping
        self.ice
        self.price

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    def __str__(self):
        return json.dumps(self.__dict__)

class TeaOrder:
    def __init__(self, count):
        self.id = str(uuid.uuid5().int)
        self.count = count
        self.boba_tea = []

    def to_json(self):
        return json.dumps(self, default=lambda o:o.__dict__,
                          sort_keys=False, indent=4)

    def add_boba(self, boba):
        self.boba_tea.append(boba)


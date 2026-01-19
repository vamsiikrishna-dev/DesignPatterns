from enum import Enum

class Order_State(Enum):
    PENDING = 1,
    SUCCESS = 2

class Order():
    def __init__(self, order_id, order_name = "", order_type = "", item_list = [], price = 100):
        self.order_id = order_id
        self.order_state = Order_State.PENDING
        self.order_name = order_name
        self.order_type = order_type
        self.item_list = item_list
        self.price = price

    def __str__(self):
        return f"order_id: {self.order_id} order_name: {self.order_name} order_state: {self.order_state}"



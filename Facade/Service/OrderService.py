from .Order import Order, Order_State
class OrderService():

    def place_order(self, item: Order):
        item.order_state = Order_State.SUCCESS
        print(f"placing order for item {item}")
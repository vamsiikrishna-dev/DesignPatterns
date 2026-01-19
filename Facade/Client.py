from Gateway import CheckoutGateway
from Service import Order

if __name__ == '__main__':

    order = Order(order_id = "order_id_123", order_name = "Iron Box", order_type = "ElectricAppliences")
    checkout_gateway = CheckoutGateway()
    checkout_gateway.place_order(order)

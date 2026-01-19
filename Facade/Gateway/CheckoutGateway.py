from Service import InventoryService, CreditCardPaymentService, OrderService, EmailNotificationService, Order


class CheckoutGateway():

    def __init__(self):
        self.inventory_service = InventoryService()
        self.payment_service = CreditCardPaymentService()
        self.order_service = OrderService()
        self.notification_service = EmailNotificationService()

    def place_order(self, order: Order):
        self.inventory_service.reserve_item(order)
        self.payment_service.pay_amount(order.price)
        self.order_service.place_order(order)
        self.notification_service.send_notification(f"Order with {order.order_id} has been placed successfully.")


        



from abc import ABC, abstractmethod

class PaymentService(ABC):

    @abstractmethod
    def pay_amount(self, amount):
        pass

class CreditCardPaymentService(PaymentService):
    
    def __init__(self, card = "12344"):
        self.card = card
    
    def pay_amount(self, amount):
        print(f"Paying amount {amount} through CreditCard")


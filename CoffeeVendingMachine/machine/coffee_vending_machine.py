from state import ReadyState, VendingMachineState
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from machine import Coffee

class CoffeeVendingMachine():
    
    def __init__(self):
        self._state = ReadyState()
        self.coffee = "Not yet decided"
        self.money_inserted = 0
    def set_state(self, state: 'VendingMachineState'):
        self._state = state
    
    def set_coffee(self, coffee: 'Coffee'):
        self.coffee = coffee
    
    def get_coffee(self):
        return self.coffee
    
    def set_money(self, money):
        self.money_inserted = money

    def get_money(self):
        return self.money_inserted

    def select_coffee(self, coffee: 'Coffee'):
        self._state.select_coffee(self, coffee)
    
    def insert_money(self, money):
        self._state.insert_money(self, money)
    
    def prepare_coffee(self, coffee: 'Coffee'):
        self._state.dispense_coffee(self, coffee)
    
    def cancel(self):
        self._state.cancel(self)
    
    def refund(self, refund_amount):
        if refund_amount > 0:
            print(f"refunding {refund_amount} rupees.")

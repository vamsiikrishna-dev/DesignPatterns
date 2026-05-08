from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from machine import Coffee

if TYPE_CHECKING:
    from machine import CoffeeVendingMachine

class VendingMachineState(ABC):

    @abstractmethod
    def select_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        pass

    @abstractmethod
    def insert_money(self, machine:'CoffeeVendingMachine', money):
        pass

    @abstractmethod
    def dispense_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        pass

    @abstractmethod
    def cancel(self, machine:'CoffeeVendingMachine'):
        pass

class ReadyState(VendingMachineState):

    def select_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print(f"selecting coffee {coffee.get_coffee_type()}")
        machine.set_coffee(coffee)
        machine.set_state(PaymentState())

    def insert_money(self, machine:'CoffeeVendingMachine', money):
        print("Please sleect coffeee")

    def dispense_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print("Please select coffee first.")

    def cancel(self, machine:'CoffeeVendingMachine'):
        print("already in ready state. so no point of cancelling")

class PaymentState(VendingMachineState):

    def select_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print(f"coffee already selected: {coffee.get_coffee_type()}")
        
    def insert_money(self, machine:'CoffeeVendingMachine', money):
        print(f"adding money {money}")
        price = machine.get_coffee().get_price()
        machine.set_money(machine.get_money() + money)
        if price <= machine.get_money():
            machine.set_state(DispenceCoffeeState())

    def dispense_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print("Please add sufficient money first.")

    def cancel(self, machine:'CoffeeVendingMachine'):
        print("Cancelling coffee")
        machine.refund(money)
        machine.set_state(ReadyState())

class DispenceCoffeeState(VendingMachineState):

    def select_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print(f"coffee already selected: {coffee.get_coffee_type()}")
        
    def insert_money(self, machine:'CoffeeVendingMachine', money):
        print("Money already paid")

    def dispense_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print("preparing coffee to dispense")
        coffee.prepare()
        machine.refund(machine.get_money() - coffee.get_price())

    def cancel(self, machine:'CoffeeVendingMachine'):
        print("Cancelling coffee")
        machine.refund(machine.get_money())
        machine.set_state(ReadyState())

class OutOfIngredientState(VendingMachineState):
    def select_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print(f"out of ingredients")
        
    def insert_money(self, machine:'CoffeeVendingMachine', money):
        print(f"out of ingredients")

    def dispense_coffee(self, machine:'CoffeeVendingMachine', coffee:'Coffee'):
        print(f"out of ingredients")

    def cancel(self, machine:'CoffeeVendingMachine'):
        machine.refund(money)
        machine.set_state(ReadyState())






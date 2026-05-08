from machine import CoffeeVendingMachine
from enums import CoffeeType
from factory import CoffeeFactory

if __name__ == '__main__':
    coffee = CoffeeFactory.create_coffee(CoffeeType.ESPRESSO)
    machine = CoffeeVendingMachine()
    machine.select_coffee(coffee)
    machine.insert_money(150)
    machine.insert_money(250)
    machine.prepare_coffee(coffee)





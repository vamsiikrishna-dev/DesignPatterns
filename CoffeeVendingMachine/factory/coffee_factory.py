from enums import CoffeeType
from machine import Espresso, Latte, Cappaccino, Coffee

class CoffeeFactory():

    @staticmethod
    def create_coffee(coffee_type: CoffeeType) -> Coffee:
        if coffee_type == CoffeeType.ESPRESSO:
            return Espresso()
        elif coffee_type == CoffeeType.LATTE:
            return Latte()
        elif coffee_type == CoffeeType.CAPPACCINO:
            return Cappaccino()
        else:
            raise Exception("Unknown coffee")

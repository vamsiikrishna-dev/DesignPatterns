from abc import ABC, abstractmethod
from typing import Dict
from enums import Ingredient, CoffeeType    

class Coffee(ABC):
    def __init__(self):
        self.coffee_type = "Unknown"

    def get_coffee_type(self):
        return self.coffee_type
    
    def prepare(self):
        print(f"\nPreparing your {self.get_coffee_type()}...")
        self._grind_beans()
        self._brew()
        self._pour_into_cup()
        print(f"{self.get_coffee_type()} is ready!")

    
    def _grind_beans(self):
        print("- Grinding fresh coffee beans")
    
    def _brew(self):
        print("- Brewing coffee with hot water")

    def _pour_into_cup(self):
        print("- Pouring into cup")

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_recipe(self):
        pass

class Espresso(Coffee):
    def __init__(self):
        super().__init__()
        self.coffee_type = CoffeeType.ESPRESSO.value
    
    def get_price(self):
        return 200
    
    def get_recipe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30}

class Latte(Coffee):
    def __init__(self):
        super().__init__()
        self.coffee_type = CoffeeType.LATTE.value

    def get_price(self):
        return 220
    
    def get_recipe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30, Ingredient.MILK: 100}

class Cappaccino(Coffee):

    def __init__(self):
        super().__init__()
        self.coffee_type = CoffeeType.LATTE
    
    def get_price(self):
        return 250
    
    def get_recipe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE_BEANS: 7, Ingredient.WATER: 30, Ingredient.MILK: 150}

    

    
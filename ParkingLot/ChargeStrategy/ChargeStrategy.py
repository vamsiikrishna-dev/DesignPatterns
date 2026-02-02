from abc import ABC, abstractmethod

class ChargeStrategy(ABC):

    @abstractmethod
    def calculate_charge(self,ticket):
        pass
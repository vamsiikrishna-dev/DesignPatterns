from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Utils import PhysicalProduct, DigitalProduct

class Visitor(ABC):

    @abstractmethod
    def visit_digital_product(self, product: 'DigitalProduct'):
        pass
    
    @abstractmethod
    def visit_physical_product(self, product: 'PhysicalProduct'):
        pass
    
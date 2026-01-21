from .Product import Product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VisitorUtil import Visitor

class PhysicalProduct(Product):
    
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def accept(self, visitor: 'Visitor'):
        visitor.visit_physical_product(self)
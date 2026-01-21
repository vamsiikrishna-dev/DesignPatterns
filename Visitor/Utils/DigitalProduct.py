from .Product import Product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VisitorUtil import Visitor

class DigitalProduct(Product):
    
    def __init__(self, name: str, price: float, file_name: str):
        self.name = name
        self.price = price
        self.file_name = file_name

    def accept(self, visitor: 'Visitor'):
        visitor.visit_digital_product(self)
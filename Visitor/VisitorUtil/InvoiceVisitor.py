from .Visitor import Visitor

class InvoiceVisitor(Visitor):
    
    def __init__(self):
        self.total = 0.0

    def visit_digital_product(self, digital_product):
        print(f"Printing Invoice for Digital Product: {digital_product.name} - ${digital_product.price}")
        self.total += digital_product.price

    def visit_physical_product(self, physical_product):
        print(f"Printing Invoice for Physical Product: {physical_product.name} - ${physical_product.price}")
        self.total += physical_product.price
    
    def get_total(self):
        return self.total
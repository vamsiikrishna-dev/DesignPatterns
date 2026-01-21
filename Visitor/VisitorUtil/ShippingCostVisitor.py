from .Visitor import Visitor

class ShippingCostVisitor(Visitor):
    
    def __init__(self):
        self.total = 0.0

    def visit_digital_product(self, digital_product):
        cost = 0.0  # Digital products have no shipping cost
        print(f"Calculating Shipping Cost for Digital Product: {digital_product.name} - ${cost}")
        self.total += cost

    def visit_physical_product(self, physical_product):
        cost = physical_product.weight * 5.0  # $5 per kg
        print(f"Calculating Shipping Cost for Physical Product: {physical_product.name} - ${cost}")
        self.total += cost
    
    def get_total(self):
        return self.total
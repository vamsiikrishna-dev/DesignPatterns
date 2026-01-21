from Utils import DigitalProduct, PhysicalProduct
from VisitorUtil import InvoiceVisitor, ShippingCostVisitor

if __name__ == '__main__':
    products = [
        DigitalProduct("Java Tutorial", 29.99, "java.pdf"),
        PhysicalProduct("MacBook", 1999.99, 2.5),
        PhysicalProduct("iPhone", 999.99, 0.3)
    ]

    invoice_visitor = InvoiceVisitor()
    shipping_cost_visitor = ShippingCostVisitor()

    for product in products:
        product.accept(invoice_visitor)
        product.accept(shipping_cost_visitor)

    print(f"Invoice Total: ${invoice_visitor.get_total():.2f}")
    print(f"Shipping Cost Total: ${shipping_cost_visitor.get_total():.2f}")

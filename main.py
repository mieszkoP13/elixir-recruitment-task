from decimal import Decimal
from models import OrderItem, Order

if __name__ == "__main__":
    # Example usage
    items = [
        OrderItem(net_price=Decimal("100.00"), quantity=2),
        OrderItem(net_price=Decimal("50.00"), quantity=3),
    ]
    order = Order(items)
    order.calculate_totals(Decimal("23")) # example 23% VAT

    print("Netto:", order.net_total)
    print("Podatek:", order.tax)
    print("Brutto:", order.total)

import unittest
from decimal import Decimal
from models import Order, OrderItem

class TestOrderCalculations(unittest.TestCase):
    def test_order_calculation(self):
        items = [
            OrderItem(net_price=Decimal("100.00"), quantity=2),
            OrderItem(net_price=Decimal("50.00"), quantity=3),
        ]
        order = Order(items)
        order.calculate_totals(Decimal("23"))  # example 23% VAT

        self.assertEqual(order.net_total, Decimal("350.00"))
        self.assertEqual(order.tax, Decimal("80.50"))
        self.assertEqual(order.total, Decimal("430.50"))

        self.assertEqual(items[0].net_total, Decimal("200.00"))
        self.assertEqual(items[0].total, Decimal("246.00"))

        self.assertEqual(items[1].net_total, Decimal("150.00"))
        self.assertEqual(items[1].total, Decimal("184.50"))

if __name__ == "__main__":
    unittest.main()

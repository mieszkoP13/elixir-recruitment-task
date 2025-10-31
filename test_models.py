import unittest
from decimal import Decimal
from models import Order, OrderItem

class TestOrderCalculations(unittest.TestCase):

    def test_single_item(self):
        """Test calculation for a single order item"""
        item = OrderItem(net_price=Decimal("100.00"), quantity=1)
        order = Order([item])
        order.calculate_totals(Decimal("23"))

        self.assertEqual(order.net_total, Decimal("100.00"))
        self.assertEqual(order.tax, Decimal("23.00"))
        self.assertEqual(order.total, Decimal("123.00"))
        self.assertEqual(item.net_total, Decimal("100.00"))
        self.assertEqual(item.total, Decimal("123.00"))

    def test_multiple_items(self):
        """Test calculation for multiple items with different prices and quantities"""
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

    def test_zero_quantity(self):
        """Test calculation for an order item with zero quantity"""
        item = OrderItem(net_price=Decimal("100.00"), quantity=0)
        order = Order([item])
        order.calculate_totals(Decimal("23"))

        self.assertEqual(order.net_total, Decimal("0.00"))
        self.assertEqual(order.tax, Decimal("0.00"))
        self.assertEqual(order.total, Decimal("0.00"))
        self.assertEqual(item.net_total, Decimal("0.00"))
        self.assertEqual(item.total, Decimal("0.00"))

    def test_zero_tax(self):
        """Test calculation with 0% tax"""
        items = [OrderItem(net_price=Decimal("50.00"), quantity=2)]
        order = Order(items)
        order.calculate_totals(Decimal("0"))

        self.assertEqual(order.net_total, Decimal("100.00"))
        self.assertEqual(order.tax, Decimal("0.00"))
        self.assertEqual(order.total, Decimal("100.00"))
        self.assertEqual(items[0].total, Decimal("100.00"))

    def test_full_tax(self):
        """Test calculation with 100% tax"""
        items = [OrderItem(net_price=Decimal("50.00"), quantity=2)]
        order = Order(items)
        order.calculate_totals(Decimal("100"))

        self.assertEqual(order.net_total, Decimal("100.00"))
        self.assertEqual(order.tax, Decimal("100.00"))
        self.assertEqual(order.total, Decimal("200.00"))
        self.assertEqual(items[0].total, Decimal("200.00"))

    def test_total_matches_sum(self):
        """Check that order total equals sum of all item totals"""
        items = [
            OrderItem(net_price=Decimal("10.00"), quantity=1),
            OrderItem(net_price=Decimal("20.00"), quantity=2),
            OrderItem(net_price=Decimal("30.00"), quantity=3),
        ]
        order = Order(items)
        order.calculate_totals(Decimal("10"))  # 10% VAT

        # Initialize sum
        sum_item_totals = Decimal("0.00")

        # Loop over all items and add their total
        for item in items:
            sum_item_totals += item.total

        self.assertEqual(order.total, sum_item_totals)

if __name__ == "__main__":
    unittest.main()

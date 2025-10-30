from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass, field
from typing import List

@dataclass
class OrderItem:
    net_price: Decimal
    quantity: int
    net_total: Decimal = field(init=False)
    total: Decimal = field(init=False)

    def calculate_totals(self, tax_rate: Decimal):
        """Calc net_total and total (gross) for this item with given tax rate"""
        # net total (net_price * quantity)
        self.net_total = (self.net_price * Decimal(self.quantity)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        # tax amount for the item
        tax_amount = (self.net_total * tax_rate / Decimal(100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        # total (gross)
        self.total = (self.net_total + tax_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return tax_amount

@dataclass
class Order:
    items: List[OrderItem]
    net_total: Decimal = field(init=False)
    tax: Decimal = field(init=False)
    total: Decimal = field(init=False)

    def calculate_totals(self, tax_rate: Decimal):
        """Calc total net, tax, and gross for the whole order."""
        self.net_total = Decimal("0.00")
        self.tax = Decimal("0.00")
        self.total = Decimal("0.00")

        # Calc totals for each item and accumulate
        for item in self.items:
            tax_amount = item.calculate_totals(tax_rate)
            self.net_total += item.net_total
            self.tax += tax_amount
            self.total += item.total

        # Round to 2 decimal places
        self.net_total = self.net_total.quantize(Decimal("0.01"))
        self.tax = self.tax.quantize(Decimal("0.01"))
        self.total = self.total.quantize(Decimal("0.01"))

"""
orders.py

Defines Order and OrderItem classes.
"""

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Product
    from customers import Customer


class OrderItem:
    """Represents a line item within a finalized order (price locked in)."""

    def __init__(self, product: "Product", quantity: int,
                 unit_price: Optional[float] = None):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price if unit_price is not None else product.price

    def calculate_subtotal(self) -> float:
        return self.unit_price * self.quantity

    def __repr__(self) -> str:
        return f"OrderItem(product='{self.product.name}', qty={self.quantity})"


class Order:
    """Represents a placed order."""

    STATUS_PENDING = "pending"
    STATUS_CANCELLED = "cancelled"
    STATUS_COMPLETED = "completed"

    def __init__(self, order_id: int, customer: "Customer",
                 items: Optional[List[OrderItem]] = None):
        self.order_id = order_id
        self.customer = customer
        self.items: List[OrderItem] = items if items is not None else []
        self.status = self.STATUS_PENDING
        self.total = self.calculate_total()

    def calculate_total(self) -> float:
        self.total = sum(item.calculate_subtotal() for item in self.items)
        return self.total

    def display_order(self) -> None:
        print(f"Order #{self.order_id} - Customer: {self.customer.name} - Status: {self.status}")
        for item in self.items:
            print(f"  - {item.product.name} x{item.quantity} @ ${item.unit_price:.2f} "
                  f"= ${item.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

    def cancel_order(self) -> None:
        if self.status == self.STATUS_CANCELLED:
            print(f"Order #{self.order_id} is already cancelled.")
            return
        self.status = self.STATUS_CANCELLED
        # Restock any physical products tied to this order.
        for item in self.items:
            if hasattr(item.product, "update_stock"):
                item.product.update_stock(item.quantity)

    def __repr__(self) -> str:
        return f"Order(id={self.order_id}, customer='{self.customer.name}', status='{self.status}')"
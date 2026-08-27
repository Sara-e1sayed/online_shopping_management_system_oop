"""
customers.py

Defines the Customer class.
"""

from __future__ import annotations
from typing import List, TYPE_CHECKING

from cart import Cart

if TYPE_CHECKING:
    from models import Product
    from orders import Order


class Customer:
    """Represents a customer of the shopping system."""

    def __init__(self, customer_id: int, name: str, email: str, phone: str = ""):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.cart: Cart = Cart()
        self.orders: List["Order"] = []

    def add_to_cart(self, product: "Product", quantity: int = 1) -> None:
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product_id: int) -> None:
        self.cart.remove_item(product_id)

    def view_cart(self) -> Cart:
        return self.cart

    def get_order_history(self) -> List["Order"]:
        return self.orders

    def __repr__(self) -> str:
        return f"Customer(id={self.customer_id}, name='{self.name}')"

    def __str__(self) -> str:
        return self.name
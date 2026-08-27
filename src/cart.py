"""
cart.py

Defines Cart and CartItem classes.
"""

from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Product


class CartItem:
    """Represents a single line item (product + quantity) within a cart."""

    def __init__(self, product: "Product", quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def update_quantity(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"CartItem(product='{self.product.name}', qty={self.quantity})"


class Cart:
    """Represents a customer's shopping cart."""

    def __init__(self):
        self.items: List[CartItem] = []

    def add_item(self, product: "Product", quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id: int) -> None:
        self.items = [item for item in self.items
                       if item.product.product_id != product_id]

    def update_item_quantity(self, product_id: int, quantity: int) -> None:
        for item in self.items:
            if item.product.product_id == product_id:
                item.update_quantity(quantity)
                return
        raise ValueError(f"Product id {product_id} not found in cart.")

    def calculate_total(self) -> float:
        return sum(item.calculate_subtotal() for item in self.items)

    def display_cart(self) -> None:
        if not self.items:
            print("Cart is empty.")
            return
        print("Cart contents:")
        for item in self.items:
            print(f"  - {item.product.name} x{item.quantity} = ${item.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

    def clear_cart(self) -> None:
        self.items = []

    def __repr__(self) -> str:
        return f"Cart(items={len(self.items)})"
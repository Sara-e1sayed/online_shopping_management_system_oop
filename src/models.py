"""
models.py

Product-related classes for the online shopping system:
Category, Product, PhysicalProduct, DigitalProduct.
"""

from __future__ import annotations
from typing import Optional


class Category:
    """Represents a product category."""

    def __init__(self, category_id: int, name: str, description: str = ""):
        self.category_id = category_id
        self.name = name
        self.description = description

    def update_name(self, new_name: str) -> None:
        self.name = new_name

    def update_description(self, new_description: str) -> None:
        self.description = new_description

    def __repr__(self) -> str:
        return f"Category(id={self.category_id}, name='{self.name}')"

    def __str__(self) -> str:
        return self.name


class Product:
    """Base class representing a generic product."""

    def __init__(self, product_id: int, name: str, price: float,
                 category: Optional[Category] = None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def get_details(self) -> str:
        category_name = self.category.name if self.category else "Uncategorized"
        return (f"[{self.product_id}] {self.name} - ${self.price:.2f} "
                f"(Category: {category_name})")

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def is_available(self, quantity: int) -> bool:
        """Base products are assumed always available (no stock tracking)."""
        return quantity > 0

    def __repr__(self) -> str:
        return f"Product(id={self.product_id}, name='{self.name}')"

    def __str__(self) -> str:
        return self.name


class PhysicalProduct(Product):
    """A product that has physical stock and weight (needs shipping)."""

    def __init__(self, product_id: int, name: str, price: float,
                 category: Optional[Category] = None,
                 stock_quantity: int = 0, weight: float = 0.0):
        super().__init__(product_id, name, price, category)
        self.stock_quantity = stock_quantity
        self.weight = weight

    def update_stock(self, quantity: int) -> None:
        """Adjust stock by a (possibly negative) quantity delta."""
        new_stock = self.stock_quantity + quantity
        if new_stock < 0:
            raise ValueError("Stock quantity cannot go negative.")
        self.stock_quantity = new_stock

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base} | Physical | Stock: {self.stock_quantity} | Weight: {self.weight}kg"

    def is_available(self, quantity: int) -> bool:
        return 0 < quantity <= self.stock_quantity


class DigitalProduct(Product):
    """A product delivered digitally (no physical stock)."""

    def __init__(self, product_id: int, name: str, price: float,
                 category: Optional[Category] = None,
                 file_size: float = 0.0, file_format: str = "",
                 download_url: str = ""):
        super().__init__(product_id, name, price, category)
        self.file_size = file_size
        self.file_format = file_format
        self.download_url = download_url

    def get_details(self) -> str:
        base = super().get_details()
        return (f"{base} | Digital | Format: {self.file_format} | "
                f"Size: {self.file_size}MB")

    # Digital products have unlimited availability -> Product.is_available
    # (quantity > 0) is sufficient, so no override is needed here beyond
    # the base behavior.
"""
system.py

Defines the ShoppingSystem class — the central coordinator, corresponding
to OnlineShoppingSystem in the class diagram.
"""

from __future__ import annotations
from typing import List, Optional

from models import Category, Product, PhysicalProduct
from customers import Customer
from orders import Order, OrderItem


class ShoppingSystem:
    """Central system tying together categories, products, customers, and orders."""

    def __init__(self):
        self.categories: List[Category] = []
        self.products: List[Product] = []
        self.customers: List[Customer] = []
        self.orders: List[Order] = []
        self._next_order_id = 1

    # ---------- Category management ----------
    def add_category(self, category: Category) -> None:
        self.categories.append(category)

    # ---------- Product management ----------
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: int) -> bool:
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def update_product(self, product_id: int, **kwargs) -> bool:
        """Update arbitrary attributes of a product (e.g. name=, price=)."""
        for product in self.products:
            if product.product_id == product_id:
                for key, value in kwargs.items():
                    if key == "price":
                        product.update_price(value)
                    elif hasattr(product, key):
                        setattr(product, key, value)
                return True
        return False

    def search_product(self, name: str) -> Optional[Product]:
        name_lower = name.lower()
        for product in self.products:
            if name_lower in product.name.lower():
                return product
        return None

    # ---------- Customer management ----------
    def register_customer(self, customer: Customer) -> None:
        self.customers.append(customer)

    # ---------- Order management ----------
    def create_order(self, customer_id: int) -> Optional[Order]:
        customer = self._find_customer(customer_id)
        if customer is None:
            print(f"Customer id {customer_id} not found.")
            return None
        if not customer.cart.items:
            print(f"Cannot create order: {customer.name}'s cart is empty.")
            return None

        order_items = []
        for cart_item in customer.cart.items:
            product = cart_item.product
            if not product.is_available(cart_item.quantity):
                print(f"Product '{product.name}' is not available in the requested quantity.")
                return None
            order_items.append(OrderItem(product, cart_item.quantity, product.price))

        # Deduct stock for physical products now that the order is confirmed.
        for order_item in order_items:
            if isinstance(order_item.product, PhysicalProduct):
                order_item.product.update_stock(-order_item.quantity)

        order = Order(self._next_order_id, customer, order_items)
        self._next_order_id += 1

        self.orders.append(order)
        customer.orders.append(order)
        customer.cart.clear_cart()
        return order

    def cancel_order(self, order_id: int) -> bool:
        for order in self.orders:
            if order.order_id == order_id:
                order.cancel_order()
                return True
        return False

    # ---------- Display helpers ----------
    def display_products(self) -> None:
        if not self.products:
            print("No products available.")
            return
        print("Products:")
        for product in self.products:
            print(f"  {product.get_details()}")

    def display_customers(self) -> None:
        if not self.customers:
            print("No customers registered.")
            return
        print("Customers:")
        for customer in self.customers:
            print(f"  [{customer.customer_id}] {customer.name} ({customer.email})")

    def display_orders(self) -> None:
        if not self.orders:
            print("No orders placed.")
            return
        print("Orders:")
        for order in self.orders:
            order.display_order()

    # ---------- Internal helpers ----------
    def _find_customer(self, customer_id: int) -> Optional[Customer]:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
"""
main.py

Demonstration script for the Online Shopping System.
"""

from models import Category, PhysicalProduct, DigitalProduct
from customers import Customer
from system import ShoppingSystem


WIDTH = 80


# ============================================================
# Display Helpers
# ============================================================

def banner(title: str) -> None:
    print("\n" + "=" * WIDTH)
    print(f"  {title}")
    print("=" * WIDTH)


def section(title: str) -> None:
    print(f"\n--- {title} ---")


# ============================================================
# Main
# ============================================================

def main():

    system = ShoppingSystem()

    banner("ONLINE SHOPPING SYSTEM")


    # ========================================================
    # STEP 1 - Categories
    # ========================================================

    banner("STEP 1 - CATEGORIES")

    electronics = Category(
        1,
        "Electronics",
        "Electronic devices and gadgets"
    )

    accessories = Category(
        2,
        "Accessories",
        "Computer and phone accessories"
    )

    books = Category(
        3,
        "Books",
        "Physical books"
    )

    ebooks = Category(
        4,
        "E-Books",
        "Digital books and courses"
    )

    categories = (
        electronics,
        accessories,
        books,
        ebooks
    )

    for category in categories:
        system.add_category(category)

    section("Created Categories")

    for category in system.get_categories():
        print(
            f"[{category.get_category_id()}] "
            f"{category.get_name()} - "
            f"{category.get_description()}"
        )


    # ========================================================
    # STEP 2 - Products
    # ========================================================

    banner("STEP 2 - PRODUCTS")

    # ---------------- Physical Products ----------------

    laptop = PhysicalProduct(
        101,
        "Gaming Laptop",
        1499.99,
        electronics,
        stock_quantity=10,
        weight=2.4
    )

    phone = PhysicalProduct(
        102,
        "Smartphone",
        799.99,
        electronics,
        stock_quantity=20,
        weight=0.2
    )

    headphones = PhysicalProduct(
        103,
        "Wireless Headphones",
        149.99,
        accessories,
        stock_quantity=30,
        weight=0.3
    )

    keyboard = PhysicalProduct(
        104,
        "Mechanical Keyboard",
        89.99,
        accessories,
        stock_quantity=15,
        weight=0.9
    )

    python_book = PhysicalProduct(
        105,
        "Python Programming Book",
        59.99,
        books,
        stock_quantity=8,
        weight=0.7
    )

    # ---------------- Digital Products ----------------

    python_course = DigitalProduct(
        201,
        "Python Programming Course",
        29.99,
        ebooks,
        file_size=850.5,
        file_format="MP4",
        download_url="https://example.com/python-course"
    )

    ml_guide = DigitalProduct(
        202,
        "Machine Learning Guide",
        24.99,
        ebooks,
        file_size=12.8,
        file_format="PDF",
        download_url="https://example.com/ml-guide"
    )

    deep_learning_course = DigitalProduct(
        203,
        "Deep Learning Course",
        39.99,
        ebooks,
        file_size=1200.0,
        file_format="MP4",
        download_url="https://example.com/deep-learning"
    )

    products = (
        laptop,
        phone,
        headphones,
        keyboard,
        python_book,
        python_course,
        ml_guide,
        deep_learning_course
    )

    for product in products:
        system.add_product(product)

    section("Product Catalog")

    for product in system.get_products():
        print(f"  {product.get_details()}")


    # ========================================================
    # STEP 3 - Customers
    # ========================================================

    banner("STEP 3 - CUSTOMERS")

    alice = Customer(
        1,
        "Alice Johnson",
        "alice@example.com",
        "555-1001"
    )

    bob = Customer(
        2,
        "Bob Smith",
        "bob@example.com",
        "555-1002"
    )

    charlie = Customer(
        3,
        "Charlie Brown",
        "charlie@example.com",
        "555-1003"
    )

    diana = Customer(
        4,
        "Diana Wilson",
        "diana@example.com",
        "555-1004"
    )

    customers = (
        alice,
        bob,
        charlie,
        diana
    )

    for customer in customers:
        system.register_customer(customer)

    section("Registered Customers")

    for customer in system.get_customers():
        print(
            f"[{customer.get_customer_id()}] "
            f"{customer.get_name()} | "
            f"{customer.get_email()} | "
            f"{customer.get_phone()}"
        )


    # ========================================================
    # STEP 4 - Shopping Carts
    # ========================================================

    banner("STEP 4 - SHOPPING CARTS")

    # Alice
    alice.add_to_cart(laptop, 1)
    alice.add_to_cart(headphones, 2)
    alice.add_to_cart(python_course, 1)

    # Bob
    bob.add_to_cart(phone, 1)
    bob.add_to_cart(keyboard, 2)
    bob.add_to_cart(ml_guide, 1)

    # Charlie
    charlie.add_to_cart(python_book, 2)
    charlie.add_to_cart(python_course, 1)

    # Diana
    diana.add_to_cart(headphones, 3)
    diana.add_to_cart(deep_learning_course, 1)

    section("Alice's Cart")
    print(alice.get_cart().display_cart())

    section("Bob's Cart")
    print(bob.get_cart().display_cart())

    section("Charlie's Cart")
    print(charlie.get_cart().display_cart())

    section("Diana's Cart")
    print(diana.get_cart().display_cart())


    # ========================================================
    # STEP 5 - Cart Operations
    # ========================================================

    banner("STEP 5 - CART OPERATIONS")

    section("Update Alice's Cart")

    alice.get_cart().update_item_quantity(
        headphones.get_product_id(),
        3
    )

    print("Wireless Headphones quantity changed to 3.")

    print(alice.get_cart().display_cart())

    section("Remove Bob's Keyboard")

    bob.remove_from_cart(
        keyboard.get_product_id()
    )

    print(bob.get_cart().display_cart())


    # ========================================================
    # STEP 6 - Product Search
    # ========================================================

    banner("STEP 6 - PRODUCT SEARCH")

    search_terms = (
        "laptop",
        "python",
        "headphones",
        "machine",
        "unknown"
    )

    for term in search_terms:

        result = system.search_product(term)

        if result:
            print(
                f"Search: '{term}'"
            )
            print(
                f"  Found: {result.get_details()}"
            )
        else:
            print(
                f"Search: '{term}'"
            )
            print(
                "  No product found."
            )


    # ========================================================
    # STEP 7 - Update Product
    # ========================================================

    banner("STEP 7 - PRODUCT UPDATE")

    old_price = headphones.get_price()

    system.update_product(
        headphones.get_product_id(),
        price=129.99
    )

    print(
        f"Product   : {headphones.get_name()}"
    )

    print(
        f"Old Price : ${old_price:.2f}"
    )

    print(
        f"New Price : ${headphones.get_price():.2f}"
    )


    # ========================================================
    # STEP 8 - Stock Operations
    # ========================================================

    banner("STEP 8 - STOCK OPERATIONS")

    section("Laptop Stock")

    print(
        f"Initial stock : "
        f"{laptop.get_stock_quantity()}"
    )

    laptop.update_stock(5)

    print(
        f"After adding 5 : "
        f"{laptop.get_stock_quantity()}"
    )

    laptop.update_stock(-2)

    print(
        f"After removing 2 : "
        f"{laptop.get_stock_quantity()}"
    )


    # ========================================================
    # STEP 9 - Product Availability
    # ========================================================

    banner("STEP 9 - PRODUCT AVAILABILITY")

    availability_tests = (
        (laptop, 1),
        (laptop, 100),
        (headphones, 5),
        (keyboard, 10),
        (python_course, 100),
        (ml_guide, 1)
    )

    for product, quantity in availability_tests:

        available = product.is_available(quantity)

        print(
            f"{product.get_name():30}"
            f" | Requested: {quantity:3}"
            f" | Available: {available}"
        )


    # ========================================================
    # STEP 10 - Create Orders
    # ========================================================

    banner("STEP 10 - CREATE ORDERS")

    alice_order, alice_msg = system.create_order(
        alice.get_customer_id()
    )

    bob_order, bob_msg = system.create_order(
        bob.get_customer_id()
    )

    charlie_order, charlie_msg = system.create_order(
        charlie.get_customer_id()
    )

    diana_order, diana_msg = system.create_order(
        diana.get_customer_id()
    )

    section("Created Orders")

    orders = (
        alice_order,
        bob_order,
        charlie_order,
        diana_order
    )

    for order in orders:

        if order:

            print(
                f"Order #{order.get_order_id():<3}"
                f" | Customer: "
                f"{order.get_customer().get_name():<15}"
                f" | Total: "
                f"${order.get_total():>8.2f}"
                f" | Status: "
                f"{order.get_status()}"
            )


    # ========================================================
    # STEP 11 - Order Details
    # ========================================================

    banner("STEP 11 - ORDER DETAILS")

    print(system.display_orders())


    # ========================================================
    # STEP 12 - Stock After Orders
    # ========================================================

    banner("STEP 12 - STOCK AFTER ORDERS")

    physical_products = (
        laptop,
        phone,
        headphones,
        keyboard,
        python_book
    )

    for product in physical_products:

        print(
            f"{product.get_name():30}"
            f" | Stock: "
            f"{product.get_stock_quantity()}"
        )


    # ========================================================
    # STEP 13 - Cancel Order
    # ========================================================

    banner("STEP 13 - CANCEL ORDER")

    if alice_order:

        print(
            f"Order #{alice_order.get_order_id()} "
            f"before cancellation:"
        )

        print(
            f"  Status: "
            f"{alice_order.get_status()}"
        )

        print(
            f"  Laptop stock: "
            f"{laptop.get_stock_quantity()}"
        )

        cancelled, cancel_msg = system.cancel_order(
            alice_order.get_order_id()
        )

        print(f"\n{cancel_msg}")

        print(
            f"\nOrder #{alice_order.get_order_id()} "
            f"after cancellation:"
        )

        print(
            f"  Status: "
            f"{alice_order.get_status()}"
        )

        print(
            f"  Laptop stock: "
            f"{laptop.get_stock_quantity()}"
        )


    # ========================================================
    # STEP 14 - Order History
    # ========================================================

    banner("STEP 14 - ORDER HISTORY")

    for customer in customers:

        print(
            f"\n{customer.get_name()}"
        )

        history = customer.get_order_history()

        if not history:
            print("  No orders.")
            continue

        for order in history:

            print(
                f"  Order #{order.get_order_id()}"
                f" | Status: {order.get_status()}"
                f" | Total: ${order.get_total():.2f}"
            )


    # ========================================================
    # STEP 15 - Product Removal Safety
    # ========================================================

    banner("STEP 15 - PRODUCT REMOVAL SAFETY")

    section("Attempt to remove a product still in a pending order")

    # Bob's order (still pending) contains the phone, so this must
    # be refused to avoid leaving a pending order pointing at a
    # deleted product.
    blocked = system.remove_product(phone.get_product_id())
    print(
        f"Remove '{phone.get_name()}' "
        f"(referenced in {bob.get_name()}'s pending order): "
        f"{'removed' if blocked else 'blocked'}"
    )

    section("Remove a product that was never ordered")

    # The keyboard was taken out of Bob's cart before checkout, so
    # it never ended up in any order and can be removed freely.
    allowed = system.remove_product(keyboard.get_product_id())
    print(
        f"Remove '{keyboard.get_name()}' "
        f"(never part of an order): "
        f"{'removed' if allowed else 'blocked'}"
    )


    # ========================================================
    # STEP 16 - Final System Summary
    # ========================================================

    banner("STEP 16 - SYSTEM SUMMARY")

    print(
        f"Categories : {len(system.get_categories())}"
    )

    print(
        f"Products   : {len(system.get_products())}"
    )

    print(
        f"Customers  : {len(system.get_customers())}"
    )

    print(
        f"Orders     : {len(system.get_orders())}"
    )


    # ========================================================
    # Finished
    # ========================================================

    print("\n" + "=" * WIDTH)
    print("  DEMO COMPLETED SUCCESSFULLY")
    print("=" * WIDTH)


if __name__ == "__main__":
    main()
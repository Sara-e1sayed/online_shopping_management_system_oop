"""
main.py

Demonstration script for the online shopping system.
No class definitions here — just usage of the classes defined in the
other modules.
"""

from models import Category, PhysicalProduct, DigitalProduct
from customers import Customer
from system import ShoppingSystem


def main():
    system = ShoppingSystem()

    # --- Set up categories ---
    electronics = Category(1, "Electronics", "Gadgets and devices")
    ebooks = Category(2, "E-Books", "Digital reading material")
    system.add_category(electronics)
    system.add_category(ebooks)

    # --- Set up products ---
    laptop = PhysicalProduct(101, "Laptop", 999.99, electronics,
                              stock_quantity=10, weight=2.1)
    headphones = PhysicalProduct(102, "Wireless Headphones", 149.99, electronics,
                                  stock_quantity=25, weight=0.3)
    ebook = DigitalProduct(201, "Python Programming Guide", 19.99, ebooks,
                            file_size=15.5, file_format="PDF",
                            download_url="https://example.com/downloads/python-guide.pdf")

    system.add_product(laptop)
    system.add_product(headphones)
    system.add_product(ebook)

    print("=" * 60)
    system.display_products()

    # --- Register customers ---
    alice = Customer(1, "Alice Johnson", "alice@example.com", "555-1234")
    bob = Customer(2, "Bob Smith", "bob@example.com", "555-5678")
    system.register_customer(alice)
    system.register_customer(bob)

    print("=" * 60)
    system.display_customers()

    # --- Shopping cart activity ---
    alice.add_to_cart(laptop, 1)
    alice.add_to_cart(headphones, 2)
    alice.add_to_cart(ebook, 1)

    print("=" * 60)
    print(f"{alice.name}'s cart:")
    alice.view_cart().display_cart()

    bob.add_to_cart(ebook, 1)

    # --- Searching products ---
    print("=" * 60)
    found = system.search_product("laptop")
    if found:
        print(f"Search result for 'laptop': {found.get_details()}")

    # --- Update a product ---
    print("=" * 60)
    system.update_product(102, price=129.99)
    print(f"Updated headphones price: ${headphones.price:.2f}")

    # --- Creating orders ---
    print("=" * 60)
    alice_order = system.create_order(alice.customer_id)
    bob_order = system.create_order(bob.customer_id)

    print("=" * 60)
    system.display_orders()

    # --- Stock effect after order ---
    print("=" * 60)
    print(f"Laptop stock after Alice's order: {laptop.stock_quantity}")

    # --- Cancel an order ---
    print("=" * 60)
    if alice_order:
        print(f"Cancelling order #{alice_order.order_id}...")
        system.cancel_order(alice_order.order_id)
        print(f"Laptop stock after cancellation: {laptop.stock_quantity}")

    print("=" * 60)
    system.display_orders()

    # --- Order history ---
    print("=" * 60)
    print(f"{alice.name}'s order history: {alice.get_order_history()}")


if __name__ == "__main__":
    main()
<div align="center">
    <h1>🛒 Online Shopping Management System 🛒</h1>
</div>

---

## Developed by

| Names |
| ------- |
| Ahmed Hossam |
| Kareem Hesham |
| Rofaida Samy |
| Sara Elsayed |
| Sara Fouda |
| Ahmed Mohamed |

---

## 1. Problem Description

<!--
اكتبوا هنا 3-5 أسطر بتشرحوا:
- إيه المشكلة اللي المشروع بيحلها؟
- مين بيستخدم النظام؟ (Customer, Shop owner)
- إيه أهم حاجة بيقدر النظام يعملها؟
مثال تقدروا تعدلوا عليه:
-->

This project simulates a simple **online store backend** using pure Python and Object-Oriented Programming.
It allows the shop to manage its **products** (physical and digital), organize them into **categories**,
register **customers**, let each customer build a **shopping cart**, and turn that cart into a confirmed
**order** with a calculated total. The system also validates simple business rules, such as preventing an
order when a physical product is out of stock.

---

## 🧩 2. Classes

<!-- لكل كلاس: سطر أو اتنين بيشرحوا مسؤوليتها. عدلوا الوصف لو غيرتوا حاجة في الكود -->

| Class | Responsibility |
| ------- | ------- |
| `Category` | Represents a group of products (e.g. Electronics, Books). |
| `Product` | Base class for any item sold in the store (id, name, price, category). |
| `PhysicalProduct` | A product with real stock and shipping cost (inherits `Product`). |
| `DigitalProduct` | A product with no stock limit and a download link (inherits `Product`). |
| `Customer` | Represents a shopper: personal info, their cart, and their order history. |
| `Cart` | Holds a list of `CartItem`, calculates the running total before checkout. |
| `CartItem` | A single product + quantity inside a cart. |
| `Order` | A confirmed purchase created from a cart, holding a list of `OrderItem`. |
| `OrderItem` | A single product + quantity + price at the time of the order. |
| `ShoppingSystem` | The central manager: owns all customers, products, categories and orders, and coordinates every operation between them. |

---

## 📦 3. Modules

<!-- اتأكدوا إن الأسماء دي مطابقة لأسماء الملفات الفعلية عندكم -->

| Module | Contains |
| ------- | ------- |
| `models.py` | `Category`, `Product`, `PhysicalProduct`, `DigitalProduct` |
| `customers.py` | `Customer` |
| `cart.py` | `Cart`, `CartItem` |
| `orders.py` | `Order`, `OrderItem` |
| `system.py` | `ShoppingSystem` |
| `main.py` | Demonstration script (no class definitions) |

---

## 🔗 4. Relationships

<!-- شرح فعلي لكل علاقة، مش بس جدول تيك. مثال جاهز تعدلوا عليه: -->

- **`Product` → `Category`**: every product belongs to exactly one category.
- **`PhysicalProduct` / `DigitalProduct` → `Product`**: both inherit from `Product` and override `get_details()`; `PhysicalProduct` also overrides `is_available()` to check real stock.
- **`Customer` → `Cart`**: each customer owns exactly one cart (composition — the cart doesn't exist without the customer).
- **`Cart` → `CartItem`**: a cart holds many cart items; each item points to one product.
- **`Customer` → `Order`**: a customer can have many past orders (order history).
- **`Order` → `OrderItem`**: an order holds many order items, copied from the cart at checkout time.
- **`ShoppingSystem`**: holds and coordinates all customers, products, categories, and orders — it's the only class that creates or cancels an order.

---

## ▶️ 5. How to Run the Project

```bash
# from the project's root folder
python main.py
```

No external libraries are required — only the Python standard library.

---

## 🖥️ 6. Example Output

<!--
شغلوا main.py وانسخوا جزء من النتيجة هنا (بين ```)
مثال شكل الحتة اللي المفروض تتحط هنا:
-->

```
--- Products ---
[101] Wireless Mouse | Price: 350 EGP | Category: Electronics | Type: Physical | Stock: 20 | Shipping: 4.0 EGP
[102] Python Crash Course (eBook) | Price: 200 EGP | Category: Books | Type: Digital | Format: PDF | Size: 15MB

--- Cart for Ahmed ---
Wireless Mouse x2 = 700 EGP
Cart Total: 700 EGP

--- Order #1 Created ---
Customer: Ahmed
Total: 700 EGP
Status: Placed
```

---

## 🧠 7. OOP Concepts Used

<!-- عدلوا الأمثلة حسب اللي فعليًا عملتوه -->

| Concept | Where it's used |
| ------- | ------- |
| **Encapsulation** | Product attributes (price, stock) are only changed through methods like `update_price()`, `update_stock()`, not accessed directly. |
| **Inheritance** | `PhysicalProduct` and `DigitalProduct` inherit from `Product`; `super().__init__()` is used to reuse the parent constructor. |
| **Polymorphism** | `is_available()` and `get_details()` behave differently depending on whether the object is a `PhysicalProduct` or a `DigitalProduct`, called the same way from `ShoppingSystem`. |
| **Composition** | A `Customer` owns one `Cart`; a `Cart` owns its `CartItem` objects — they don't exist independently. |
| **Modularity** | The system is split across 6 files, each with a clear responsibility, and classes are imported where needed. |

---

## 📊 8. Diagrams

<!-- حطوا هنا لينك أو صورة الـ class diagram بعد ما يتظبط خالص -->

See `class_diagram.png` in the project folder.

---

## 📈 9. Project Progress Tracker

> *For internal team use — update while working. This is not part of the final grading criteria, just to help the team stay organized.*

### Classes

| Task | Status |
| ------- | ------- |
| `1.` Category | ⏳ |
| `2.` Product (base) | ⏳ |
| `3.` PhysicalProduct | ⏳ |
| `4.` DigitalProduct | ⏳ |
| `5.` Customer | ⏳ |
| `6.` CartItem | ⏳ |
| `7.` Cart | ⏳ |
| `8.` OrderItem | ⏳ |
| `9.` Order | ⏳ |
| `10.` ShoppingSystem | ⏳ |

### Modules

| Task | Status |
| ------- | ------- |
| `1.` models.py | ⏳ |
| `2.` customers.py | ⏳ |
| `3.` cart.py | ⏳ |
| `4.` orders.py | ⏳ |
| `5.` system.py | ⏳ |
| `6.` main.py | ⏳ |

### Required System Features

| Task | Status |
| ------- | ------- |
| `1.` Create / Register | ⏳ |
| `2.` Display | ⏳ |
| `3.` Relationship Operation | ⏳ |
| `4.` Calculation | ⏳ |
| `5.` Search | ⏳ |
| `6.` Update | ⏳ |
| `7.` Remove / Delete | ⏳ |
| `8.` Validation | ⏳ |

### main.py Demo Steps

| Task | Status |
| ------- | ------- |
| `1.` Import all classes | ⏳ |
| `2.` Create ShoppingSystem | ⏳ |
| `3.` Add categories | ⏳ |
| `4.` Add products (Physical + Digital) | ⏳ |
| `5.` Add 2+ customers | ⏳ |
| `6.` Add products to a cart | ⏳ |
| `7.` Display cart + total | ⏳ |
| `8.` Create order from cart | ⏳ |
| `9.` Display order | ⏳ |
| `10.` Display customer order history | ⏳ |
| `11.` Cancel one order | ⏳ |
| `12.` Validation case (out of stock) | ⏳ |

### Documentation & Deliverables

| Task | Status |
| ------- | ------- |
| `1.` Code comments added | ⏳ |
| `2.` Class/Module diagram | ⏳ |
| `3.` README.md | ⏳ |
| `4.` Presentation slides | ⏳ |
| `5.` Working demo tested | ⏳ |

---

## 🚫 10. Restrictions Followed

```py
input()          ❌ not used anywhere
Database / SQL   ❌ not used
Flask / Django   ❌ not used
GUI              ❌ not used
Authentication   ❌ not used
```
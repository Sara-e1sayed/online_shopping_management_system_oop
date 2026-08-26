<div align="center">
    <h1>🛒 Online Shopping Management System 🛒</h1>
</div>

## Developed by:
| Names |
| ------- |
| Ahmed Hossam |
| Kareem |
| Rofaida Samy |
| Sara Elsayed |
| Sara Fouda |
| Ahmed Mohamed |


## 1. Classes

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

---

## 2. Modules

| Task | Status |
| ------- | ------- |
| `1.` models.py (Category, Product, PhysicalProduct, DigitalProduct) | ⏳ |
| `2.` customers.py (Customer) | ⏳ |
| `3.` cart.py (Cart, CartItem) | ⏳ |
| `4.` orders.py (Order, OrderItem) | ⏳ |
| `5.` system.py (ShoppingSystem) | ⏳ |
| `6.` main.py (demo) | ⏳ |

---

## 3. Inheritance

| Task | Status |
| ------- | ------- |
| `1.` Product base class | ⏳ |
| `2.` PhysicalProduct inherits Product | ⏳ |
| `3.` DigitalProduct inherits Product | ⏳ |
| `4.` super().__init__() used correctly | ⏳ |

---

## 4. Relationships | Diagrams

| Task | Status |
| ------- | ------- |
| `1.` Product → Category | ⏳ |
| `2.` CartItem → Product | ⏳ |
| `3.` Cart → CartItems | ⏳ |
| `4.` Customer → Cart | ⏳ |
| `5.` OrderItem → Product | ⏳ |
| `6.` Order → OrderItems | ⏳ |
| `7.` Customer → Orders | ⏳ |

---

## 5. Required System Features

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

---

## 6. main.py Demo Steps

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

---

## 7. Documentation & Deliverables

| Task | Status |
| ------- | ------- |
| `1.` Code comments added | ⏳ |
| `2.` Class/Module diagram | ⏳ |
| `3.` README.md | ⏳ |
| `4.` Presentation slides | ⏳ |
| `5.` Working demo tested | ⏳ |

---

## 8. Important Restriction
```py
input () ❌ 
```

## 9. Module Requirements
```txt
project/
├── main.py
├── models.py
├── customers.py
├── cart.py
├── orders.py
└── system.py
```
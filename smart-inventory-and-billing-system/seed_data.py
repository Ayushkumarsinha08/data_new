from faker import Faker
import random
from database import conn

fake = Faker("en_IN")

cur = conn.cursor()

# Customers
for _ in range(30):
    cur.execute("""
        INSERT INTO customers (name, contact)
        VALUES (%s, %s)
    """, (
        fake.name(),
        fake.phone_number()[:10]
    ))

conn.commit()

print("30 customers inserted")

products = [
    ("Dell Inspiron 15", "Laptop", 55000),
    ("HP Pavilion 14", "Laptop", 60000),
    ("Lenovo IdeaPad Slim 3", "Laptop", 48000),
    ("Acer Aspire 5", "Laptop", 45000),
    ("ASUS VivoBook 15", "Laptop", 52000),
    ("Logitech Wireless Mouse", "Mouse", 799),
    ("HP Wired Mouse", "Mouse", 399),
    ("Dell Keyboard", "Keyboard", 899),
    ("Mechanical Keyboard", "Keyboard", 2499),
    ("USB Hub", "Accessory", 699),
    ("Laptop Stand", "Accessory", 999),
    ("Samsung 1TB SSD", "Storage", 5999),
    ("WD 2TB HDD", "Storage", 4999),
    ("SanDisk 128GB Pendrive", "Storage", 799),
    ("Kingston 64GB Pendrive", "Storage", 499),
    ("Dell 24 Inch Monitor", "Monitor", 12999),
    ("LG 27 Inch Monitor", "Monitor", 18999),
    ("Samsung Curved Monitor", "Monitor", 24999),
    ("Acer Gaming Monitor", "Monitor", 21999),
    ("Boat Rockerz Headphones", "Audio", 1999),
    ("JBL Bluetooth Speaker", "Audio", 3499),
    ("Sony Earbuds", "Audio", 4999),
    ("Noise Earbuds", "Audio", 2499),
    ("TP-Link Router", "Networking", 2499),
    ("D-Link Router", "Networking", 1999),
    ("WiFi Range Extender", "Networking", 1499),
    ("Network Switch", "Networking", 2999),
    ("Power Bank 10000mAh", "Mobile Accessory", 999),
    ("Power Bank 20000mAh", "Mobile Accessory", 1799),
    ("USB-C Cable", "Cable", 299),
    ("Lightning Cable", "Cable", 499),
    ("Fast Charger 25W", "Charger", 799),
    ("Fast Charger 65W", "Charger", 1499),
    ("Canon Printer", "Printer", 9999),
    ("HP Printer", "Printer", 11999),
    ("Webcam HD", "Camera", 1499),
    ("Webcam Full HD", "Camera", 2999),
    ("Smart Watch", "Wearable", 3999),
    ("Fitness Band", "Wearable", 1999),
    ("Laptop Cooling Pad", "Accessory", 899)
]

for product in products:
    cur.execute("""
        INSERT INTO products (name, description, price, quantity)
        VALUES (%s, %s, %s, %s)
    """, (
        product[0],
        product[1],
        product[2],
        random.randint(20,100)
    ))

conn.commit()

print("40 products inserted")

for _ in range(50):

    customer_id = random.randint(1,30)

    cur.execute("""
        INSERT INTO sales
        (customer_id, date, total_amount)
        VALUES (%s, CURRENT_DATE - (%s * INTERVAL '1 day'), 0)
        RETURNING id
    """, (
        customer_id,
        random.randint(1,90)
    ))

    sale_id = cur.fetchone()[0]

    total = 0

    items_count = random.randint(1,4)

    for _ in range(items_count):

        product_id = random.randint(1,40)

        quantity = random.randint(1,3)

        cur.execute(
            "SELECT price FROM products WHERE id=%s",
            (product_id,)
        )

        price = float(cur.fetchone()[0])

        cur.execute("""
            INSERT INTO sale_items
            (sale_id, product_id, quantity, price)
            VALUES (%s,%s,%s,%s)
        """, (
            sale_id,
            product_id,
            quantity,
            price
        ))

        total += quantity * price

    cur.execute("""
        UPDATE sales
        SET total_amount=%s
        WHERE id=%s
    """, (
        total,
        sale_id
    ))

conn.commit()

print("50 sales inserted")
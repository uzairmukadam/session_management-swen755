import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "../../database/ecommerce.db")


def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, price REAL)"""
    )

    # Clear existing products to avoid duplicates
    c.execute("DELETE FROM products")

    # Add dummy products
    products = [
        ("Product 1", 19.99),
        ("Product 2", 29.99),
        ("Product 3", 39.99),
        ("Product 4", 49.99),
        ("Product 5", 59.99),
        ("Product 6", 69.99),
        ("Product 7", 79.99),
        ("Product 8", 89.99),
        ("Product 9", 99.99),
        ("Product 10", 109.99),
    ]
    c.executemany("INSERT INTO products (title, price) VALUES (?, ?)", products)

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    # Convert product tuples to dictionaries
    products_dicts = [{"id": p[0], "title": p[1], "price": p[2]} for p in products]
    return products_dicts


def get_product_by_id(product_id):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product


def get_user_by_username(username):
    # This function would normally interact with a real user database.
    # For simplicity, we are using a predefined dictionary of users.
    return users.get(username)

from db import get_connection
from passlib.context import CryptContext

# Parollarni xesh qilish uchun context yaratamiz
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    if cur.fetchone():
        print("\nUser already exists.")
    else:
        hashed_password = pwd_context.hash(password)
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("\nUser registered successfully.")
    cur.close()
    conn.close()

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, password, is_admin FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user and pwd_context.verify(password, user[1]):
        print("\nLogin successful.")
        return {'user_id': user[0], 'is_admin': user[2]}
    else:
        print("\nInvalid credentials.")
        return None

def add_product(name, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    cur.close()
    conn.close()
    print("\nProduct added.")

def list_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products")
    products = cur.fetchall()
    cur.close()
    conn.close()
    print("\nProduct List:")
    for p in products:
        print(f"ID: {p[0]} | Name: {p[1]} | Price: ${p[2]:.2f}")

def add_to_cart(user_id, product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO cart (user_id, product_id) VALUES (%s, %s)", (user_id, product_id))
    conn.commit()
    cur.close()
    conn.close()
    print("\nProduct added to cart.")

def view_cart(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT products.id, products.name, products.price
        FROM cart
        JOIN products ON cart.product_id = products.id
        WHERE cart.user_id = %s
    ''', (user_id,))
    items = cur.fetchall()
    cur.close()
    conn.close()
    print("\nYour Cart:")
    for i in items:
        print(f"Product ID: {i[0]} | Name: {i[1]} | Price: ${i[2]:.2f}")

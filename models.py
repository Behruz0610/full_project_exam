from db import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(80) UNIQUE NOT NULL,
        password VARCHAR(200) NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(120) NOT NULL,
        price FLOAT NOT NULL
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        product_id INTEGER REFERENCES products(id)
    );
    ''')
    conn.commit()
    cur.close()
    conn.close()

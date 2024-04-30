import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

# Создаем таблицу товаров
cur.execute('''
CREATE TABLE IF NOT EXISTS tovari (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Создаем таблицу поставщиков
cur.execute('''
CREATE TABLE IF NOT EXISTS postavchiki (
    id INTEGER PRIMARY KEY,
    company_name TEXT,
    contact_info TEXT
)
''')

# Создаем таблицу заказов
cur.execute('''
CREATE TABLE IF NOT EXISTS zakazi (
    id INTEGER PRIMARY KEY,
    supplier_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    status TEXT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
)
''')

# Заполняем таблицы данными
cur.execute('''
INSERT INTO tovari (name, quantity, price) VALUES
('Product A', 100, 10.99),
('Product B', 50, 20.50),
('Product C', 75, 15.75)
''')

cur.execute('''
INSERT INTO postavchiki (company_name, contact_info) VALUES
('Supplier X', '123-456-7890'),
('Supplier Y', '234-567-8901'),
('Supplier Z', '345-678-9012')
''')

cur.execute('''
INSERT INTO zakazi (supplier_id, order_date, quantity, status) VALUES
(1, '2024-01-15', 50, 'pending'),
(2, '2024-02-02', 30, 'shipped'),
(3, '2024-03-10', 25, 'delivered')
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()


# Выборка данных из таблицы заказов
conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

cur.execute('SELECT * FROM zakazi')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
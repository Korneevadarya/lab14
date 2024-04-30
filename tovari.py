import sqlite3

# Выборка данных из таблицы товаров
conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

cur.execute('SELECT * FROM tovari')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
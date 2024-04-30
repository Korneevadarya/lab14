import sqlite3

# Выборка данных из таблицы поставщиков
conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

cur.execute('SELECT * FROM postavchiki')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
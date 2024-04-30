import sqlite3
# Выборка данных из таблицы заказов
conn = sqlite3.connect('warehouse.db')
cur = conn.cursor()

cur.execute('SELECT * FROM zakazi')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
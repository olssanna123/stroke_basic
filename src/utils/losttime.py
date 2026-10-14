
import sqlite3

conn = sqlite3.connect("output/latest.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM iterations WHERE status = ?", ("lost",))
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
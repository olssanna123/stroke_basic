import sqlite3

# Anslut till databasen
conn = sqlite3.connect("output/ideal10000.db")
cursor = conn.cursor()

# Hämta alla värden från kolumnen time
cursor.execute("SELECT time FROM iterations")

# Spara värdena i en Python-lista
times = [row[0] for row in cursor.fetchall()]

# Stäng anslutningen
conn.close()

print(times)
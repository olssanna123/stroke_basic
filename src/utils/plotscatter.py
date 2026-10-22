
import sqlite3
import matplotlib.pyplot as plt

# Anslut till databasen
conn = sqlite3.connect("output/latest.db")
cursor = conn.cursor()

# Hämta id och tid där status är 'lost'
cursor.execute(
    "SELECT id, time FROM iterations WHERE status = ?",
    ("lost",)
)

rows = cursor.fetchall()
conn.close()

# Dela upp id och tid
ids = [row[0] for row in rows]
times = [row[1] for row in rows]

print(f"IDs: {ids}")
print(f"Times: {times}")

# Plotta id mot tid
plt.figure(figsize=(10, 6))
plt.scatter(ids, times, alpha=0.7)
plt.xlabel("ID")
plt.ylabel("Time")
plt.title("Time vs ID (status = lost)")
plt.grid(True)
plt.tight_layout()

plt.savefig("scatter_plot.png", dpi=300)
plt.show()
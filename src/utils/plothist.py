
import sqlite3
import matplotlib.pyplot as plt

# Anslut till databasen
conn = sqlite3.connect("output/spec50utannegn1000.db")
cursor = conn.cursor()

# Hämta alla tider där status är 'lost'
#cursor.execute("SELECT time FROM iterations")
cursor.execute(
        "SELECT id, time FROM iterations WHERE status = ?",
        ("lost",)
    )


times = [row[0] for row in cursor.fetchall()]
print(f"Times: {times}")

# Stäng anslutningen
conn.close()


# Plotta histogram
plt.hist(times, bins=20, edgecolor="black")

plt.xlabel("Tid (s)")
plt.ylabel("Antal patienter")
plt.title("Histogram över förlorad tid för ett instrument med 50% specificitet, N=1000, behandlingstid 30 min")
plt.grid(axis="y", alpha=0.3)

plt.show()

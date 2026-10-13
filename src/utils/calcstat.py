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

import statistics
from scipy import stats
import math

n = len(times)

if n < 2:
    raise ValueError("Det behövs minst två observationer.")

# Stickprovsmedelvärde
medelvarde = statistics.mean(times)

# Stickprovsvarians
stickprovsvarians = statistics.variance(times)

# Stickprovsstandardavvikelse
stickprovsstandardavvikelse = statistics.stdev(times)

# 95 % konfidensintervall
t_kritiskt = stats.t.ppf(0.975, df=n - 1)

marginal = t_kritiskt * stickprovsstandardavvikelse / math.sqrt(n)

nedre_grans = medelvarde - marginal
ovre_grans = medelvarde + marginal

# Skriv ut resultaten
print(f"Stickprovsmedelvärde: {medelvarde:.6f}")
print(f"Stickprovsvarians: {stickprovsvarians:.6f}")
print(f"Stickprovsstandardavvikelse: {stickprovsstandardavvikelse:.6f}")
print(f"95 % konfidensintervall: [{nedre_grans:.6f}, {ovre_grans:.6f}]")

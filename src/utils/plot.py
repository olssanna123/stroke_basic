import matplotlib.pyplot as plt
import sqlite3
from src.database.connection import get_connection

def plot_time_vs_id():
    # Hämta data från databasen
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, time FROM iterations")
    resultat = cursor.fetchall()

    # Dela upp värdena i två listor
    id_lista = [rad[0] for rad in resultat]
    time_lista = [rad[1] for rad in resultat]

    # Rita diagrammet
    plt.figure(figsize=(10, 5))
    plt.plot(id_lista, time_lista, marker='o', linestyle='-')

    plt.xlabel("ID")
    plt.ylabel("Time")
    plt.title("Time för varje ID")
    plt.grid(True)
    plt.tight_layout()
    plt.show()  

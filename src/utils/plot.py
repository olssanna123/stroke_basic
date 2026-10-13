
import matplotlib.pyplot as plt
from src.database.connection import get_connection

def plot_time_vs_id():
    # Hämta endast data med status "saved"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, time FROM iterations WHERE status = ?",
        ("saved",)
    )
    resultat = cursor.fetchall()

    # Dela upp värdena i två listor
    id_lista = [rad[0] for rad in resultat]
    time_lista = [rad[1] for rad in resultat]

    # Rita diagrammet
    plt.figure(figsize=(10, 5))
    plt.scatter(id_lista, time_lista)

    plt.xlabel("Patient nummer (ID)")
    plt.ylabel("Time (s)")
    plt.title(
        "Spridningsdiagram för sparad tid, N = 1000, "
        "50% Specificitet, behandlingstid 30 min"
    )
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    conn.close()

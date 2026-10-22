
import matplotlib.pyplot as plt
from src.database.connection import get_connection

def plot_time_vs_id():
    # Hämta data
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, time FROM iterations"
    )
    resultat = cursor.fetchall()

    # Dela upp värdena i två listor
    id_lista = [rad[0] for rad in resultat]
    time_lista = [rad[1] / 60 for rad in resultat]  # Sekunder till minuter

    # Rita diagrammet
    plt.figure(figsize=(10, 5))
    plt.scatter(id_lista, time_lista)

    plt.xlabel("Patient nummer (ID)")
    plt.ylabel("Tid (minuter)")
    plt.title(
        "Spridningsdiagram för sparad tid, N = 1000, "
        "80% sensitivitet, behandlingstid 30 min"
    )

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("scatter_plot.png", dpi=300)
    plt.show()

    conn.close()

plot_time_vs_id()
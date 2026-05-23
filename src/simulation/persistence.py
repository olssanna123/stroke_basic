import sqlite3
from pathlib import Path

DB_PATH = Path("runs/latest.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def save_iteration(iteration, municipality, response_time):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO iterations (
            iteration,
            municipality,
            response_time
        )
        VALUES (?, ?, ?)
    """, (iteration, municipality, response_time))

    conn.commit()
    conn.close()
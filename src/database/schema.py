from src.database import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS iterations (
            id INTEGER PRIMARY KEY,
            iteration INTEGER,
            municipality TEXT,
            response_time REAL
        )
    """)

    conn.commit()
    conn.close()
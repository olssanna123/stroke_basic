from src.database import get_connection


def insert_iteration(iteration, municipality, response_time):
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

def get_all_iterations():
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT * FROM iterations
    """).fetchall()

    conn.close()

    return rows
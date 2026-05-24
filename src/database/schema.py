from src.database.connection import get_connection


def create_tables(config):
    conn = get_connection()
    cursor = conn.cursor()
    match config.variable:
        case "none": 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS iterations (
                    id INTEGER PRIMARY KEY,
                    iteration INTEGER,
                    latitude REAL,
                    longitude REAL,
                    municipality TEXT,
                    emergency_hospital TEXT,
                    triage_rule TEXT,
                    patient_to_emergency_hospital REAL,
                    emergency_hospital_to_academic_hospital REAL,
                    patient_to_academic_hospital REAL,
                    variable TEXT,
                    time REAL
                )
            """)
        case "sensitivity":
            pass
        case "specificity":
            pass
        case _:
            print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
    conn.commit()
    conn.close()
    return

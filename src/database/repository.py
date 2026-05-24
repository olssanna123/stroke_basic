from src.database.connection import get_connection


def insert_iteration(config, iteration, results):
    conn = get_connection()
    cursor = conn.cursor()

    match config.variable:
        case "none":             
            cursor.execute("""
                INSERT INTO iterations (
                    iteration,
                    latitude,
                    longitude,
                    municipality,
                    emergency_hospital,
                    triage_rule,
                    patient_to_emergency_hospital,
                    emergency_hospital_to_academic_hospital,
                    patient_to_academic_hospital,
                    variable,
                    time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (iteration, results["latitude"], results["longitude"], results["municipality"], results["emergency_hospital"], results["triage_rule"], results["patient_to_emergency_hospital"], results["emergency_hospital_to_academic_hospital"], results["patient_to_academic_hospital"], results["variable"], results["time"]))
        case "sensitivity":
            pass
        case "specificity":
            pass
        case _:
            print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
            return

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

def table_info():
    conn = get_connection()
    cursor = conn.cursor()

    info = cursor.execute("""
        PRAGMA table_info(iterations)
    """).fetchall()

    conn.close()
    print(info)
    return 

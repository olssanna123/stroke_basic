from sqlalchemy import func

from src.data.db import SessionLocal
from src.models import Simulation, SimulationResult


def create_simulation(name: str, total_iterations: int) -> int:
    """
    Skapar en ny simulation och returnerar simulation_id.
    """

    with SessionLocal() as session:

        simulation = Simulation(
            name=name,
            total_iterations=total_iterations,
            status="running",
        )

        session.add(simulation)
        session.commit()

        # Efter commit finns ID automatiskt
        session.refresh(simulation)

        return simulation.id


def get_start_iteration(session, simulation_id: int) -> int:
    """
    Hittar senaste sparade iteration för återupptagning.
    """

    last_iteration = (
        session.query(func.max(SimulationResult.iteration))
        .filter(
            SimulationResult.simulation_id == simulation_id
        )
        .scalar()
    )

    if last_iteration is None:
        return 0

    return last_iteration + 1


def run_single_iteration(iteration: int):
    """
    Här gör du själva simuleringen.
    Ersätt med din egen logik.
    """

    result = {
        "patient_id": 1,
        "hospital_id": 2,
        "rule_id": 1,
        "time_seconds": 420,
        "category": "red",
        "patient_to_acute": 120,
        "acute_to_academic": 240,
        "patient_to_academic": 360,
    }

    return result


def run_simulation(simulation_id: int):
    """
    Kör eller återupptar simulation.
    """

    with SessionLocal() as session:

        simulation = session.get(
            Simulation,
            simulation_id,
        )

        if simulation is None:
            raise ValueError("Simulation not found")

        start_iteration = get_start_iteration(
            session,
            simulation_id,
        )

        total_iterations = simulation.total_iterations

    print(
        f"Starting from iteration "
        f"{start_iteration}/{total_iterations}"
    )

    try:

        for iteration in range(
            start_iteration,
            total_iterations,
        ):

            # NY SESSION PER ITERATION
            with SessionLocal() as session:

                try:

                    result = run_single_iteration(iteration)

                    db_result = SimulationResult(
                        simulation_id=simulation_id,
                        iteration=iteration,

                        patient_id=result["patient_id"],
                        hospital_id=result["hospital_id"],
                        rule_id=result["rule_id"],

                        time_seconds=result["time_seconds"],
                        category=result["category"],

                        patient_to_acute=result["patient_to_acute"],
                        acute_to_academic=result["acute_to_academic"],
                        patient_to_academic=result["patient_to_academic"],
                    )

                    session.add(db_result)

                    session.commit()

                    print(
                        f"Saved iteration {iteration}"
                    )

                except Exception:

                    session.rollback()

                    print(
                        f"Failed iteration {iteration}"
                    )

                    raise

        # Markera simulation som klar
        with SessionLocal() as session:

            simulation = session.get(
                Simulation,
                simulation_id,
            )

            simulation.status = "completed"

            session.commit()

        print("Simulation completed")

    except Exception:

        # Markera simulation som failed
        with SessionLocal() as session:

            simulation = session.get(
                Simulation,
                simulation_id,
            )

            simulation.status = "failed"

            session.commit()

        print("Simulation failed")

        raise


if __name__ == "__main__":

    simulation_id = create_simulation(
        name="Monte Carlo Test",
        total_iterations=10000,
    )

    run_simulation(simulation_id)
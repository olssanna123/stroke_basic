from simulation.persistence import save_iteration

for i in range(1000):

    response_time = run_simulation()

    save_iteration(
        iteration=i,
        municipality="Göteborg",
        response_time=response_time
    )
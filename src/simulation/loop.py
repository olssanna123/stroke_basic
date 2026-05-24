from src.simulation.pipeline import run_single_iteration

def run_loop(config, array):    
    for i in range(config.n_iterations):
        print(f"Running iteration {i+1}/{config.n_iterations}")
        result = run_single_iteration(config, array)    
        print(f"Iteration {i+1}/{config.n_iterations} completed")
        
    return
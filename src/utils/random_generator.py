import numpy as np

# Pseudo-random number generator. Seed used for reproducibility.
rng = np.random.default_rng()

# Return random integer between 0 and highest_number
def model(highest_number):
    return rng.integers(0, highest_number)
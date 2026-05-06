from sampling.pipeline import sample_location
from routing.triage import triage_patient
from simulation.outcome import simulate_detection
from simulation.metrics import compute_metrics

def run_single_iteration(config, data):

    # 1. Slumpa plats
    point = sample_location(data)

    # 2. Triage (här sker beslutet från flödesschemat)
    routing = triage_patient(point, data, config)

    # 3. Simulera om trombektomi identifieras korrekt
    detected = simulate_detection(
        is_true_case=True,
        sensitivity=config.sensitivity,
        specificity=config.specificity
    )

    # 4. Beräkna tid
    metrics = compute_metrics(point, routing, config, detected)

    return metrics
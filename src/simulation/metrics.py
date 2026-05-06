def compute_metrics(point, routing, config, detected):

    if not detected:
        return {
            "status": "missed",
            "time_loss": routing["travel_times"]["to_su"]
        }

    return {
        "status": "detected",
        "chosen": routing["chosen"]
    }
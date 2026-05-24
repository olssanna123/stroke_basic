# Hanterar simulering och loop vid eventuella avbrott och återupptar simuleringen från där den slutade.

from src.database.repository import insert_iteration


def accepted_iteration(config, iteration, results):
    insert_iteration(config, iteration, results)
    return
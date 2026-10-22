from dataclasses import dataclass
from src.models.variable import Variable

@dataclass
class Config:
    n_iterations: int =  1000   # Ange antalet iterationer, n = 100, 1000, eller 10000

    variable: Variable = Variable.SENSITIVITY  # Ange vilken variabel som ska variera, "sensitivity" eller "none" (100% för både sensitivity och specificity)
    sensitivity: int = 80    # Ange sensitivitet 90%, 80%, 50%
    specificity: int = 50   # Ange specificitet 90%, 80%, 50%

    su_threshold_minutes: int = 45
    comparison_threshold_minutes: int = 15

    akut_treatment_time: int = 30  

# Obs! Variablerna su_threshold_minutes, comparison_threshold_minutes och akut_treatment_time anges som minuter för enkelhet för användaren
# Vid jämförelse converteras de till sekunder för att jämföra med resultat från OSRM 
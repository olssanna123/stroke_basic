from dataclasses import dataclass

@dataclass
class Config:
    n_iterations: int = 1000    # Ange antalet iterationer, n = 100, 1000, eller 10000

    variable: str = "none"  # Ange vilken variabel som ska variera, "sensitivity","specificity" eller "none"
    sensitivity: float = 0.9    # Ange sensitivitet, 1 = 100%, 0.9 = 90%, 0.8 = 80%, 0.5 = 50%
    specificity: float = 0.85   # Ange specificitet, 1 = 100%, 0.9 = 90%, 0.8 = 80%, 0.5 = 50%

    su_threshold_minutes: int = 45
    comparison_threshold_minutes: int = 15

    akut_treatment_time: int = 30  

# Obs! Variablerna su_threshold_minutes, comparison_threshold_minutes och akut_treatment_time anges som minuter för enkelhet för användaren
# Vid jämförelse converteras de till sekunder för att jämföra med resultat från OSRM 
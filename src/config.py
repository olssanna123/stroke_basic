from dataclasses import dataclass

@dataclass
class Config:
    n_iterations: int = 3    # Ange antalet iterationer, n = 10, 100, 1000, eller 10000

    variable: str = "none"  # Ange vilken variabel som ska variera, "sensitivity","specificity" eller "none" (100% för både sensitivity och specificity)
    sensitivity: int = 90    # Ange sensitivitet 90%, 80%, 50%
    specificity: int = 90   # Ange specificitet 90%, 80%, 50%

    su_threshold_minutes: int = 45
    comparison_threshold_minutes: int = 15

    akut_treatment_time: int = 30  

# Obs! Variablerna su_threshold_minutes, comparison_threshold_minutes och akut_treatment_time anges som minuter för enkelhet för användaren
# Vid jämförelse converteras de till sekunder för att jämföra med resultat från OSRM 
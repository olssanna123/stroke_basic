from dataclasses import dataclass

@dataclass(frozen=True)
class MetricsResult:
    patient_to_emergency_hospital: float
    emergency_hospital_to_academic_hospital: float
    patient_to_academic_hospital: float
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Result:
    latitude: float
    longitude: float
    municipality: str
    emergency_hospital: str
    triage_rule: str
    patient_to_emergency_hospital: float
    emergency_hospital_to_academic_hospital: float  
    patient_to_academic_hospital: float
    variable: str
    time: float

    def to_dict(self) -> dict:
        return asdict(self)

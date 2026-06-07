from dataclasses import dataclass

@dataclass(frozen=True)
class Patient:
    latitude: float
    longitude: float
    municipality: str
from dataclasses import dataclass
from src.models.hospital import Hospital

@dataclass(frozen=True)
class TriageResult:
    chosen_emergency_hospital: Hospital
    triage_rule: str
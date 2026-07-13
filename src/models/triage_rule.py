from dataclasses import dataclass

@dataclass(frozen=True)
class TriageRule:
    rule1: str
    rule2: str
    rule3: str
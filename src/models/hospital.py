# ------------- domänmodell --------------
from dataclasses import dataclass

@dataclass(frozen=True)
class Hospital:
    name: str
    latitude: float
    longitude: float

    def coord(self):
        return (self.latitude, self.longitude)

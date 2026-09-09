from dataclasses import dataclass
from datetime import date

@dataclass
class WeightRecord:
    date: date
    weight: float

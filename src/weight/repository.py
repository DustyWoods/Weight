from datetime import date, timedelta
from pathlib import Path

from .database import DB
from .models import WeightRecord

class Repository:

    def __init__(self, path: Path):
        self.path = path

    def add_today(self, weight: float):
        record = WeightRecord(date.today(), round(weight, 1))
        
        with DB(self.path) as db:
            db.add(record)

    def recent(self, days: int = 30):
        end = date.today()
        start = end - timedelta(days=days-1)

        with DB(self.path) as db:
            result = db.get_range(start, end)

        return result

from datetime import date, timedelta

from .database import DB
from .models import WeightRecord

class Repository:

    def __init__(self, path: str):
        self.path = path

    def add_today(self, weight: float):
        record = WeightRecord(date.today(), round(weight, 2))
        
        with DB(self.path) as db:
            db.add(record)

    def recent(self, days: int = 30):
        end = date.today()
        start = end - timedelta(days=days)

        with DB(self.path) as db:
            result = db.get_range(start, end)

        return result

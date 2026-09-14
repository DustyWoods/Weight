import os
import tempfile
import unittest
from random import uniform
from datetime import date, timedelta
from pathlib import Path

from weight.repository import Repository
from weight.database import DB
from weight.models import WeightRecord

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False)
        self.db_file.close()
        self.repository = Repository(Path(self.db_file.name))

    def tearDown(self):
        os.unlink(self.db_file.name)
    
    def test_add_today(self):
        today = date.today()
        weight = 80.35

        self.repository.add(date.today(), weight)

        result = self.repository.recent(1)

        self.assertEqual(result, [ WeightRecord(today, round(weight, 1)) ])


    def test_add(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ round(uniform(60.0, 90.0), 1) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        for weight, day in zip(weights, days):
            self.repository.add(day, weight)

        result = self.repository.recent()

        self.assertEqual(result, records)

    def test_recent(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ round(uniform(60.0, 90.0), 1) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        with DB(Path(self.db_file.name)) as db:
            for record in records:
                db.add(record)

        result = self.repository.recent()
        
        self.assertEqual(records, result)

    def test_recent_with_limited_days(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ uniform(60.0, 90.0) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        with DB(Path(self.db_file.name)) as db:
            for record in records:
                db.add(record)

        counts = range(5, 31, 5)

        for count in counts:
            with self.subTest(count=count):
                result = self.repository.recent(count)
        
                self.assertEqual(records[30-count: 30], result)

    def test_clean(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ uniform(60.0, 90.0) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        with DB(Path(self.db_file.name)) as db:
            for record in records:
                db.add(record)
            self.repository.clean()
            result = db.get_all()

        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()

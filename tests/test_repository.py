import os
import tempfile
import unittest
from random import uniform
from datetime import date, timedelta

from src.repository import Repository
from src.database import DB
from src.models import WeightRecord

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False)
        self.db_file.close()
        self.repository = Repository(self.db_file.name)

    def tearDown(self):
        os.unlink(self.db_file.name)
    
    def test_add_tody(self):
        today = date.today()
        weight = 80.35

        self.repository.add_today(weight)

        result = self.repository.recent(1)

        self.assertEqual(result, [ WeightRecord(today, round(weight, 1)) ])

    def test_recent(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ uniform(60.0, 90.0) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        with DB(self.db_file.name) as db:
            for record in records:
                db.add(record)

        result = self.repository.recent()
        
        self.assertEqual(records, result)

    def test_recent_with_limited_days(self):
        days = [ date.today() - timedelta(days=i) for i in range(29, -1, -1) ]
        weights = [ uniform(60.0, 90.0) for _ in range(30) ]

        records = [ WeightRecord(days[i], weights[i]) for i in range(30)]

        with DB(self.db_file.name) as db:
            for record in records:
                db.add(record)

        counts = range(5, 31, 5)

        for count in counts:
            with self.subTest(count=count):
                result = self.repository.recent(count)
        
                self.assertEqual(records[30-count: 30], result)

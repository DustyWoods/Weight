import unittest
from datetime import date

from src.database import DB
from src.models import WeightRecord

class TestDB(unittest.TestCase):

    def test_add(self):
        record = WeightRecord(date=date(2026, 9, 9), weight=81.1)

        with DB(":memory:") as db:
            db.init()
            db.add(record)
            records = db.get_range(date(2026, 9, 9), date(2026, 9, 9))

        self.assertEqual(records, [record])

    def test_update(self):
        first = WeightRecord(date=date(2026, 9, 9), weight=80.2)
        second = WeightRecord(date=date(2026, 9, 9), weight=78.2)

        with DB(":memory:") as db:
            db.init()
            db.add(first)
            db.add(second)
            records = db.get_range(date(2026, 9, 9), date(2026, 9, 9))

        self.assertEqual(records, [second])

    def test_get_range(self):
        records = [
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 3), 79.3),
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 5), 66.3),
        ]

        with DB(":memory:") as db:
            db.init()
            for record in records:
                db.add(record)

            result = db.get_range(date(2026, 1, 3), date(2026, 1, 4))

        self.assertEqual(result, records[1: 3])

    def test_get_range_empty(self):
        with DB(":memory:") as db:
            db.init()
            result = db.get_range(date(2026, 1, 3), date(2026, 1, 4))

        self.assertEqual(result, [])

    def test_get_range_order(self):
        records = [
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 5), 66.3),
            WeightRecord(date(2026, 1, 3), 79.3),
        ]

        expected = [
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 3), 79.3),
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 5), 66.3),
        ]

        with DB(":memory:") as db:
            db.init()
            for record in records:
                db.add(record)
            result = db.get_range(date(2026, 1, 2), date(2026, 1, 5))

        self.assertEqual(result, expected)

    def test_get_all(self):
        records = [
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 3), 79.3),
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 5), 66.3),
        ]

        with DB(":memory:") as db:
            db.init()
            for record in records:
                db.add(record)

            result = db.get_all()
        self.assertEqual(result, records)

    def test_get_all_empty(self):
        with DB(":memory:") as db:
            db.init()
            result = db.get_all()
        self.assertEqual(result, [])

    def test_get_all_order(self):
        records = [
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 5), 66.3),
            WeightRecord(date(2026, 1, 3), 79.3),
        ]

        expected = [
            WeightRecord(date(2026, 1, 2), 80.2),
            WeightRecord(date(2026, 1, 3), 79.3),
            WeightRecord(date(2026, 1, 4), 77.3),
            WeightRecord(date(2026, 1, 5), 66.3),
        ]

        with DB(":memory:") as db:
            db.init()
            for record in records:
                db.add(record)
            result = db.get_all()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

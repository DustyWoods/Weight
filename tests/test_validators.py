import unittest
from datetime import date

from weight.validators import  validate_weight, validate_date

from weight.validators import MAX_WEIGHT, MIN_WEIGHT

class TestValidateWeight(unittest.TestCase):

    def test_valid_weight(self):
        validate_weight(60.0)

    def test_min_weight(self):
        validate_weight(MIN_WEIGHT)

    def test_max_weight(self):
        validate_weight(MAX_WEIGHT)

    def test_weight_below_min(self):
        with self.assertRaises(ValueError):
            validate_weight(MIN_WEIGHT - 0.1)

    def test_weight_over_max(self):
        with self.assertRaises(ValueError):
            validate_weight(MAX_WEIGHT + 0.1)

class TestValidateDate(unittest.TestCase):

    def test_valid_date(self):
        today = date.today()
        _year = today.year
        _month = today.month

        items = [
                ["2022-02-12", date(2022,2, 12)],
                ["2023-3-2", date(2023, 3, 2)],
                ["2021-3-23", date(2021, 3, 23)],
                ["2023-12-3", date(2023, 12, 3)],
                ["12-23", date(_year, 12, 23)],
                ["2-23", date(_year, 2, 23)],
                ["12-2", date(_year, 12, 2)],
                ["2-2", date(_year, 2, 2)],
                ["2", date(_year, _month, 2)],
                ["12", date(_year, _month, 12)],
                ]

        for value, day in items:
            with self.subTest(value=value, day=day):
                result = validate_date(value)
                self.assertEqual(result, day)

    def test_invalid_date(self):
        items = [
                "123-12-12",
                "12345-12-12",
                "1234-2-30",
                "1234-13-4",
                "1344-12-34-34",
                "1234.12.12",
                "1234/12/12/"
                ]
        for item in items:
            with self.subTest(item=item):
                with self.assertRaises(ValueError):
                    validate_date(item)

if __name__ == "__main__":
    unittest.main()

import sys
import unittest
from unittest.mock import patch

from weight.parser import get_args

class TestParser(unittest.TestCase):

    def test_command(self):
        test_cases = [
            {
                "argv" : [ "weight", "add", "80.32" ],
                "command" : "add",
                "weight" : "80.32",
            },
            {
                "argv" : [ "weight", "add", "80.32", "-d", "12-12" ],
                "command" : "add",
                "weight" : "80.32",
                "date" : "12-12",
            },
            {
                "argv" : [ "weight", "add", "80.32", "--date", "12-12" ],
                "command" : "add",
                "weight" : "80.32",
                "date" : "12-12",
            },
            {
                "argv": [ "weight", "add", "-d", "12-12", "80.32"],
                "command" : "add",
                "weight" : "80.32",
                "date" : "12-12",
            },
            {
                "argv": [ "weight", "add", "--date", "12-12", "80.32"],
                "command" : "add",
                "weight" : "80.32",
                "date" : "12-12",
            },
            {
                "argv" : [ "weight", "show"],
                "command" : "show",
            },
            {
                "argv" : [ "weight", "clean" ],
                "command" : "clean",
                "force" : False,
            },
            {
                "argv" : [ "weight", "clean", "-f" ],
                "command" : "clean",
                "force" : True,
            },
            {
                "argv" : [ "weight", "clean", "--force" ],
                "command" : "clean",
                "force" : True,
            }
        ]

        for case in test_cases:
            with self.subTest(**case):
                with patch.object(sys, "argv", case["argv"]):
                    args = get_args()

                self.assertEqual(args.command, case["command"])
                if "weight" in case: 
                    self.assertEqual(args.weight, float(case["weight"]))
                if "date" in case:
                    self.assertEqual(args.date, case["date"])
                if "force" in case:
                    self.assertEqual(args.force, case["force"])

if __name__ == "__main__":
    unittest.main()

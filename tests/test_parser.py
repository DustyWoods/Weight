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
                "recent" : 30,
                "no-lines" : False,
                "no-data" : False,
                "no-graph" : False,
            },
            {
                "argv" : [ "weight", "show", "-r", "13" ],
                "command" : "show",
                "recent" : 13,
                "no-lines" : False,
                "no-data" : False,
                "no-graph" : False,
            },
            {
                "argv" : [ "weight", "show", "--recent", "12" ],
                "command" : "show",
                "recent" : 12,
                "no-lines" : False,
                "no-data" : False,
                "no-graph" : False,
            },
            {
                "argv" : [ "weight", "show", "--no-lines" ],
                "command" : "show",
                "recent" : 30,
                "no-lines" : True,
                "no-data" : False,
                "no-graph" : False,
            },
            {
                "argv" : [ "weight", "show", "--no-data" ],
                "command" : "show",
                "recent" : 30,
                "no-lines" : False,
                "no-data" : True,
                "no-graph" : False,
 
            },
            {
                "argv" : [ "weight", "show", "--no-graph" ],
                "command" : "show",
                "recent" : 30,
                "no-lines" : False,
                "no-data" : False,
                "no-graph" : True,
 
            },
            {
                "argv" : [ "weight", "show", "--recent", "11", "--no-lines", "--no-data", "--no-graph" ],
                "command" : "show",
                "recent" : 11,
                "no-lines" : True,
                "no-data" : True,
                "no-graph" : True,
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
                if "recent" in case:
                    self.assertEqual(args.recent, case['recent'])
                if "no-lines" in case:
                    self.assertEqual(args.no_lines, case["no-lines"])
                if "no-data" in case:
                    self.assertEqual(args.no_data, case["no-data"])
                if "no-graph" in case:
                    self.assertEqual(args.no_graph, case["no-graph"])
                if "force" in case:
                    self.assertEqual(args.force, case["force"])

if __name__ == "__main__":
    unittest.main()

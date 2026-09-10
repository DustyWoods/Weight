import unittest
from unittest.mock import patch

from src.parser import get_args

class TestParser(unittest.TestCase):

    @patch("sys.argv", ["weight", "add", "80.34"])
    def test_add(self):
        args = get_args()

        self.assertEqual(args.command, "add")
        self.assertEqual(args.weight, 80.34)

    @patch("sys.argv", ["weight", "show"])
    def test_show(self):
        args = get_args()

        self.assertEqual(args.command, "show")

if __name__ == "__main__":
    unittest.main()

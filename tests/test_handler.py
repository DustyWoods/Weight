import unittest
from unittest.mock import Mock

from src.handler import Handler

class TestHandler(unittest.TestCase):

    def test_add(self):
        repository = Mock()
        handler = Handler(repository)

        args = Mock()
        args.command = "add"
        args.weight = 70.38

        handler.handle(args)

        repository.add_today.assert_called_once_with(70.38)

if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import Mock, patch
from datetime import date
from argparse import Namespace

from weight.handler import Handler

class TestHandler(unittest.TestCase):

    def setUp(self):
        self.repository = Mock()
        self.handler = Handler(self.repository)

    def test_add(self):
        test_cases = [
            {
                "weight" : 80.99,
                "_date" : date.today(),
            },
            {
                "weight" : 80.99,
                "date" : "2022-12-12",
                "_date" : date(2022, 12, 12),
            },
        ]

        for case in test_cases:
            with self.subTest(**case):
                self.repository.reset_mock()

                args = Namespace(
                    command = "add",
                    weight = case["weight"],
                    date = case['date'] if 'date' in case else None
                )

                self.handler.handle(args)

                self.repository.add.assert_called_once_with(case["_date"], case["weight"])

    @patch("weight.handler.render")
    @patch("weight.handler.validate_recent")
    def test_show(self, mock_validate_recent, mock_render):
        records = []
        self.repository.recent.return_value = records

        args = Namespace(
            command = "show",
            recent = 30,
            no_lines = False,
            no_data = False,
            no_graph = False,
        )

        self.handler.handle(args)

        mock_validate_recent.assert_called_once_with(args.recent)
        self.repository.recent.assert_called_once_with(args.recent)
        mock_render.assert_called_once_with(records, days=args.recent, flag_lines=not args.no_lines, flag_data=not args.no_data, flag_graph=not args.no_graph)

    @patch("weight.handler.confirm_clean")
    def test_clean(self, mock_confirm_clean):
        test_cases = [
            {
                "force" : False,
                "confirm" : True,
            },
            {
                "force" : False,
                "confirm" : False,
            },
            {
                "force" : True,
                "confirm" : True,
            },
            {
                "force" : True,
                "confirm" : False,
            }
        ]

        print_value = "All records deleted"

        for case in test_cases:
            with self.subTest(**case):
                self.repository.reset_mock()
                mock_confirm_clean.reset_mock()

                args = Namespace(
                    command = "clean",
                    force = case["force"],
                )
                mock_confirm_clean.return_value = case['confirm']

                with patch("builtins.print") as mock_print:
                    self.handler.handle(args)
                if args.force:
                    mock_confirm_clean.assert_not_called()

                    self.repository.clean.assert_called_once_with()
                    mock_print.assert_called_once_with(print_value)
                else:
                    mock_confirm_clean.assert_called_once_with()

                    if case['confirm']:
                        self.repository.clean.assert_called_once_with()
                        mock_print.assert_called_once_with(print_value)
                    else:
                        self.repository.clean.assert_not_called()
                        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()

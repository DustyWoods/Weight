import argparse

def create_parser():
    parser = argparse.ArgumentParser(
            description="Weight Tracking Tool"
            )

    subparsers = parser.add_subparsers(
            dest="command",
            required=True
            )

    add_parser = subparsers.add_parser(
            "add",
            help="Add today's weight record (kg; rounded to one decimal place"
            )
    add_parser.add_argument(
            "weight",
            type=float
            )
    add_parser.add_argument(
            "-d",
            "--day",
            type=str,
            help="Record date in YYYY-MM-DD format (default: today)"
            )

    subparsers.add_parser(
            "show",
            help="Display the past 30 days of weight records using a line chart"
            )

    clean_parser = subparsers.add_parser(
            "clean",
            help="Clear all weight records"
            )
    clean_parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="CLear all weight records without confirmation"
            )

    return parser

def get_args():
    parser = create_parser()
    args = parser.parse_args()

    return args

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
            help="Add today's weight record (kg; rounded to one decimal place)"
            )
    add_parser.add_argument(
            "weight",
            type=float
            )

    subparsers.add_parser(
            "show",
            help="Display the past 30 days of weight records using a line chart"
            )

    return parser

def get_args():
    parser = create_parser()
    args = parser.parse_args()

    return args

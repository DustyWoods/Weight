import argparse

from .repository import Repository
from .utils import render
from .validators import validate_weight

class Handler:

    def __init__(self, repository: Repository):
        self.repository = repository

    def handle(self, args: argparse.Namespace):
    
            if args.command == "add":
                validate_weight(args.weight)
                self.repository.add_today(args.weight)
            elif args.command == "show":
                records = self.repository.recent()
                render(records)

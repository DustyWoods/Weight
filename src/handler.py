import argparse

from .repository import Repository

class Handler:

    def __init__(self, repository: Repository):
        self.repository = repository

    def handle(self, args: argparse.Namespace):
    
            if args.command == "add":
                self.repository.add_today(args.weight)
            elif args.command == "show":
                pass

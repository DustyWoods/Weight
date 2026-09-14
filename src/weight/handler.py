import argparse

from .repository import Repository
from .utils import render, confirm_clean
from .validators import validate_weight

class Handler:

    def __init__(self, repository: Repository):
        self.repository = repository

    def handle(self, args: argparse.Namespace):
    
            if args.command == "add":
                validate_weight(args.weight)
                self.repository.add(args.weight)
            elif args.command == "show":
                records = self.repository.recent()
                render(records)
            elif args.command == "clean":
                if not args.force:
                    if not confirm_clean():
                        return
                self.repository.clean()

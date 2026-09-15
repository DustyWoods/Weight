import argparse
from datetime import date

from .repository import Repository
from .utils import render, confirm_clean
from .validators import validate_weight, validate_date, validate_recent

class Handler:

    def __init__(self, repository: Repository):
        self.repository = repository

    def handle(self, args: argparse.Namespace):
    
            if args.command == "add":
                self._handle_add(args)
            elif args.command == "show":
                self._handle_show(args)
            elif args.command == "clean":
                self._handle_clean(args)

    def _handle_add(self, args):
        _date = validate_date(args.date) if args.date else date.today()
        validate_weight(args.weight)
        self.repository.add(_date, args.weight)

    def _handle_show(self, args):
        validate_recent(args.recent)
        records = self.repository.recent(args.recent)
        render(records, days = args.recent, flag_lines=not args.no_lines, flag_data=not args.no_data, flag_graph=not args.no_graph)

    def _handle_clean(self, args):
        if not args.force and not confirm_clean(): return
        self.repository.clean()
        print("All records deleted")

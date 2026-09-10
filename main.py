from pathlib import Path

from src.parser import get_args
from src.handler import Handler
from src.repository import Repository


PROJECT_ROOT = Path(__file__).resolve().parent
DB_PATH = PROJECT_ROOT / "weight.db"


def main():
    args = get_args()

    repository = Repository(DB_PATH)
    handler = Handler(repository)

    handler.handle(args)


if __name__ == "__main__":
    main()

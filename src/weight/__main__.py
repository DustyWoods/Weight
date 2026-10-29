from .parser import get_args
from .handler import Handler
from .repository import Repository
from .config import get_database_path

def main():
    args = get_args()

    db_path = get_database_path()
    if not db_path.parent.exists():
        db_path.parent.mkdir(parents=True, exist_ok=True)

    repository = Repository(db_path)
    handler = Handler(repository)

    try:
        handler.handle(args)
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

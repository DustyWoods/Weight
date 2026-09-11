from .parser import get_args
from .handler import Handler
from .repository import Repository
from .config import get_database_path

def main():
    args = get_args()

    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    repository = Repository(db_path)
    handler = Handler(repository)

    handler.handle(args)


if __name__ == "__main__":
    main()

from src.parser import get_args
from src.handler import Handler
from src.repository import Repository
from src.config import get_database_dir

def main():
    args = get_args()

    db_path = get_database_dir()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    repository = Repository(db_path)
    handler = Handler(repository)

    handler.handle(args)


if __name__ == "__main__":
    main()

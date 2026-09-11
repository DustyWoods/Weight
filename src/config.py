from pathlib import Path
from platformdirs import user_data_dir

APP_NAME="weight"

def get_data_dir():
    # Return the application data directory
    return Path(user_data_dir(APP_NAME))

def get_database_dir():
    # Return the database path
    return get_data_dir() / "weight.db"

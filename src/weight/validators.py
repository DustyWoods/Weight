import re
from datetime import date

MIN_WEIGHT = 20.0
MAX_WEIGHT = 300.0

_DATE_PATTERN= re.compile(r'^\d+(?:-\d+){0,2}$')


def validate_weight(value: float) -> None:
    '''
    Validate the value

    Raise:
        ValueError: If the value is too low or too high to be true
    '''

    if not MIN_WEIGHT <= value <= MAX_WEIGHT:
        raise ValueError(
            f"Value must be between {MIN_WEIGHT} and {MAX_WEIGHT} kg."

        )

def validate_date(value: str) -> date:
    '''
    Validate and normalize a flexible date string

    Supportted format:
        YYYY-MM-DD
        YYYY-M-DD
        YYYY-MM-D
        YYYY-M-D
        MM-DD
        M-DD
        M-D
        MM-D
        D
        DD

    Missing year/month are filled using today date

    Returns:
        A date object

    Raises:
        ValueError: If the date format is invalid or the date does not exist
    '''

    value = value.strip()

    if not _DATE_PATTERN.fullmatch(value):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD, MM-DD or DD.")

    parts = [ int(part) for part in value.split("-") ]
    today = date.today()

    if len(parts) == 3:
        year, month, day = parts

        if not 999 < year <10000:
            raise ValueError("Invalid date format. Year must be 4 digits.")

    elif len(parts) == 2:
        year = today.year
        month, day = parts

    else:
        year = today.year
        month = today.month
        day = parts[0]

    try:
        return date(year, month, day)
    except ValueError as exc:
        raise ValueError(f"Invalid date: {value}") from exc

MIN_WEIGHT = 20.0
MAX_WEIGHT = 300.0


def validate_weight(weight: float) -> None:
    if not MIN_WEIGHT <= weight <= MAX_WEIGHT:
        raise ValueError(
            f"weight must be between {MIN_WEIGHT} and {MAX_WEIGHT} kg"
        )

def get_round_number(number: str) -> str:
    """Retrieve the number without unnecessary decimals

    Args:
        number: The number to round
    Returns:
        The number rounded
    """
    if number is None or number == "":
        return None

    return ("%f" % float(number)).rstrip("0").rstrip(".")

def get_and_check_search_type(value: str) -> str:
    """Checks and retrieve the search type

    Args:
        value: The value representing the search type
    Returns:
        The search type value
    Raises:
        ValueError if the search type is not valid
    """
    from models.scraper import GitSearchType

    if not value:
        return ""

    if not hasattr(GitSearchType, getattr(value, "value", "")) and not hasattr(
        GitSearchType, value
    ):
        raise ValueError("Search type does not exist")
    return value

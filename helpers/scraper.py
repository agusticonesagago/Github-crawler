import json


def get_html_class_name(search_type: str) -> str:
    """Get the class name depending on the search type

    Args:
        search_type: The type of the search
    Returns:
        The class name belonging to the search type
    """
    from models.scraper import GitSearchType

    if search_type == GitSearchType.wikis or search_type == GitSearchType.wikis.value:
        return "Link--muted text-small text-bold"
    if search_type == GitSearchType.issues or search_type == GitSearchType.issues.value:
        return "Link--muted text-bold"

    return "v-align-middle"


def get_github_data(input_data: dict) -> dict:
    """Retrieves the GitHub data
    Args:
        input_data: The keywords, the proxies and the type of search to be done
    Returns:
        The GitHub links and in case they are repositories,
        also is retrieved the author and the percentages of languages belonging
    """
    from models.scraper import GitScraper

    search_type = input_data.get("type", "").lower()
    git_scraper = GitScraper(
        search_type=search_type,
        keywords=input_data.get("keywords", ""),
        proxies=input_data.get("proxies", ""),
    )

    git_scraper.create_git_search_url()
    dict_git_urls = git_scraper.get_git_urls(git_scraper.fetch_page())

    if search_type != "repositories" or search_type is None or search_type == "":
        return json.dumps(dict_git_urls)

    for i in range(0, len(dict_git_urls)):
        git_scraper.url = dict_git_urls[i]["url"]
        dict_git_urls[i]["extra"] = git_scraper.get_repository_extra_information(
            git_scraper.fetch_page()
        )

    return json.dumps(dict_git_urls)

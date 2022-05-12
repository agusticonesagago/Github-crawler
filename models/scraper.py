import enum
import random

import requests
from bs4 import BeautifulSoup

import settings
from helpers.number import get_round_number
from helpers.scraper import get_html_class_name
from validators.scraper import get_and_check_search_type
from collections import defaultdict


class Scraper(object):
    """The Scraper object let extract information from websites"""

    def __init__(self, url=None, content=None, proxies=None, keywords=""):
        self.url = url
        self.content = content
        self.proxies = proxies
        self.keywords = keywords

    def fetch_page(self) -> bytes:
        """Retrieves the content from the url"""
        proxy = self.get_proxy()
        proxies = {"https": "https://" + proxy, "http": "http://" + proxy}
        return requests.get(self.url, proxies=proxies).content

    def get_proxy(self) -> str:
        """Gets one random proxy from the available ones"""
        if self.proxies is None:
            return ""

        if type(self.proxies) is list:
            return random.choice(self.proxies)
        return self.proxies


class GitSearchType(enum.Enum):
    repositories = "repositories"
    issues = "issues"
    wikis = "wikis"


class GitScraper(Scraper):
    """The GitHub crawler object let extract information from the GitHub searcher"""

    def __init__(
        self, search_type="", url=None, content=None, proxies=None, keywords=""
    ):
        self.search_type = search_type
        super(GitScraper, self).__init__(url, content, proxies, keywords)

    @property
    def search_type(self) -> str:
        return self._search_type

    @search_type.setter
    def search_type(self, value) -> None:
        """Sets and check the input search type

        Args:
            self: the scraper object
            value: the value to set to search type
        Raises:
            ValueError if the search type does not exist
        """
        self._search_type = get_and_check_search_type(value)

    def create_git_search_url(self) -> None:
        """Creates the Git research url"""
        word_search = self.keywords
        if type(self.keywords) is list:
            word_search = "+".join(word_search)

        search_type = self.search_type
        if type(search_type) != str:
            search_type = getattr(self.search_type, "value", "")
        self.url = f"https://github.com/search?q={word_search}&type={search_type}"

    def get_git_urls(self, content: bytes) -> list:
        """Retrieves the git urls from a search

        Args:
            self: The git scraper object
            content: The content to where retrieve the urls
        Returns:
            The search URLs
        """
        list_urls = []

        soup = BeautifulSoup(content, "html.parser")
        for a in soup.find_all("a", get_html_class_name(self.search_type)):
            list_urls.append({"url": settings.GITHUB_URL + a["href"]})
        return list_urls

    @staticmethod
    def get_repository_extra_information(content: bytes) -> defaultdict:
        """Retrieves the repository information

        Args:
            content: The content to where retrieve the information
        Returns:
            The information retrieved, such as the repository author and the programming languages
        """
        repository_extra_information = defaultdict(str)
        repository_extra_information["language_stats"] = {}

        soup = BeautifulSoup(content, "html.parser")
        for language in soup.find_all(
            "a",
            "d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline "
            "text-small mr-3",
        ):
            repository_extra_information["language_stats"][
                language.contents[3].text
            ] = get_round_number(language.contents[5].text.replace("%", ""))

        repository_extra_information["owner"] = soup.find("a", "url fn").text

        return repository_extra_information

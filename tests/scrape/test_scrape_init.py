import pytest

from models.scraper import GitScraper, GitSearchType


@pytest.mark.integration
class TestScrapeInit:
    def test_scrape_by_repositories(self):
        git_scraper = GitScraper(search_type=GitSearchType.repositories)

        assert git_scraper.search_type == GitSearchType.repositories

    def test_scrape_by_issues(self):
        git_scraper = GitScraper(search_type=GitSearchType.issues)

        assert git_scraper.search_type == GitSearchType.issues

    def test_scrape_by_wikis(self):
        git_scraper = GitScraper(search_type=GitSearchType.wikis)

        assert git_scraper.search_type == GitSearchType.wikis

    def test_scrape_by_incorrect_search_type(self):
        try:
            GitScraper(search_type="ad")
            assert False
        except ValueError as ve:
            assert True

        try:
            git_scraper = GitScraper()
            git_scraper.search_type = "a"
            assert False
        except ValueError as ve:
            assert True

    def test_scrape_with_multiple_proxies(self):
        proxies = ["194.126.37.94:8080", "13.78.125.167:8080"]
        git_scraper = GitScraper(proxies=proxies)

        assert git_scraper.proxies == proxies
        assert git_scraper.get_proxy() in proxies

    def test_scrape_with_unique_proxy(self):
        proxy = "194.126.37.94:8080"
        git_scraper = GitScraper(proxies=proxy)

        assert git_scraper.proxies == proxy
        assert git_scraper.get_proxy() == proxy

    def test_scrape_with_multiple_keywords(self):
        keywords = ["nova", "openstack"]
        git_scraper = GitScraper(keywords=keywords)

        assert git_scraper.keywords == keywords

    def test_scrape_with_unique_keyword(self):
        keywords = "nova"
        git_scraper = GitScraper(keywords=keywords)

        assert git_scraper.keywords == keywords

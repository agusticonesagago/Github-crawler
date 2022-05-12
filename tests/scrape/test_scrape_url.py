import pytest

from models.scraper import GitScraper, GitSearchType


@pytest.mark.integration
class TestScrapeUrl:
    def test_scrape_url_with_search_words(self):
        keywords = "nova"
        git_scraper = GitScraper(keywords=keywords, search_type=GitSearchType.wikis)

        git_scraper.create_git_search_url()

        assert git_scraper.url == "https://github.com/search?q=nova&type=wikis"

    def test_scrape_url_without_search_words(self):
        git_scraper = GitScraper(search_type=GitSearchType.wikis)

        git_scraper.create_git_search_url()

        assert git_scraper.url == "https://github.com/search?q=&type=wikis"

    def test_scrape_url_without_search_type(self):
        keywords = ["nova", "css"]
        git_scraper = GitScraper(keywords=keywords)

        git_scraper.create_git_search_url()

        assert git_scraper.url == "https://github.com/search?q=nova+css&type="

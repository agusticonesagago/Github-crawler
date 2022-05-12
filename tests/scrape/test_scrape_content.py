import pytest

from models.scraper import GitScraper, GitSearchType


@pytest.mark.integration
class TestScrapeContent:
    def test_scrape_url_content(self):
        git_scraper = GitScraper(content="a", search_type=GitSearchType.wikis)

        import fileinput

        for line in fileinput.input("../files/web_content"):
            list_urls = git_scraper.get_git_urls(line)

        assert len(list_urls) == 10

    def test_scrape_repository_content(self):
        git_scraper = GitScraper(
            url="https://github.com/atuldjadhav/DropBox-Cloud-Storage",
            search_type=GitSearchType.wikis,
        )

        import fileinput

        for line in fileinput.input("../files/repository_content"):
            extra_information = git_scraper.get_repository_extra_information(line)

        assert len(extra_information) == 2
        assert (
            "owner" in extra_information and extra_information["owner"] == "atuldjadhav"
        )
        assert (
            "language_stats" in extra_information
            and len(extra_information["language_stats"]) == 3
        )

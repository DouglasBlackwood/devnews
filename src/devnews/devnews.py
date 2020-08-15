from terminaltables import SingleTable

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase

URLS = (
    "http://feeds.wired.com/wired/index",
    "http://hackaday.com/feed/",
    "http://news.ycombinator.com/rss",
    "http://rss.slashdot.org/Slashdot/slashdot",
    "http://feeds.dzone.com/home",
    "http://www.engadget.com/rss.xml",
    "http://www.reddit.com/r/gaming/.rss",
    "http://www.reddit.com/r/geek/.rss",
    "http://www.reddit.com/r/programming/.rss",
    "http://www.reddit.com/r/science/.rss",
    "http://www.reddit.com/r/scifi/.rss",
    "http://www.reddit.com/r/technology/.rss",
    "http://www.techmeme.com/index.xml",
)


def print_table(news):
    data = [(entry.source_name, entry.title) for entry in news[:10]]
    data.insert(0, ("Feed", "Title"))
    table = SingleTable(data)
    print(table.table)


if __name__ == "__main__":
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = ListNewsUseCase(*repositories)
    news = use_case.execute()
    print_table(news)

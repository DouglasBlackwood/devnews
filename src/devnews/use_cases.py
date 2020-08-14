from threading import Thread

from devnews.repositories import FeedNewsRepository

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

PARSER_TIMEOUT = 10


class ListNewsUseCase:
    def execute(self):
        threads = []
        result = []

        for url in URLS:
            thread = FeedParserThread(FeedNewsRepository(url), result)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join(timeout=PARSER_TIMEOUT)

        return tuple(result)


class FeedParserThread(Thread):
    def __init__(self, repo, result):
        self.repo, self.result = repo, result

        super().__init__()

    def run(self):
        self.result.extend(self.repo.get_all())

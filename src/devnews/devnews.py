from threading import Thread

import feedparser

URLS = (
    "http://feeds.wired.com/wired/index",
    "http://hackaday.com/feed/",
    "http://news.ycombinator.com/rss",
    "http://rss.slashdot.org/Slashdot/slashdot",
    "http://www.dzone.com/links/feed/frontpage/rss.xml",
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


def get_news():
    threads = []
    news = []

    for url in URLS:
        thread = FeedParserThread(url, news)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join(timeout=PARSER_TIMEOUT)

    return tuple(news)


class FeedParserThread(Thread):
    def __init__(self, url, news):
        self.url, self.news = url, news

        super().__init__()

    def run(self):
        feed = feedparser.parse(self.url)
        # feed_name = feed.feed.title

        for article in feed.entries:
            self.news.append(article)


if __name__ == "__main__":
    get_news()

from threading import Thread
from datetime import datetime
from time import mktime

import feedparser
from terminaltables import SingleTable

from devnews.entities import FeedEntry

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
        try:
            feed_name = feed.feed.title
        except AttributeError as e:
            print(e, self.url, feed.feed)
            raise

        for entry in feed.entries:
            feed_entry = FeedEntry(
                feed_name,
                entry.title,
                entry.link,
                entry.description,
                datetime.fromtimestamp(mktime(entry.updated_parsed)),
            )
            self.news.append(feed_entry)


def print_table(news):
    data = [(entry.feed_name, entry.title) for entry in news[:10]]
    data.insert(0, ("Feed", "Title"))
    table = SingleTable(data)
    print(table.table)


if __name__ == "__main__":
    news = get_news()
    print_table(news)

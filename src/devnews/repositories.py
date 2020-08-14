from datetime import datetime
from time import mktime

import feedparser

from devnews.interfaces import NewsRepository
from devnews.entities import Article


class FeedNewsRepository(NewsRepository):
    def __init__(self, url):
        self.url = url

    def get_all(self):
        feed = feedparser.parse(self.url)
        try:
            source_name = feed.feed.title
        except AttributeError as e:
            print(e, self.url, feed.feed)
            raise

        news = []

        for entry in feed.entries:
            feed_entry = Article(
                source_name,
                entry.title,
                entry.link,
                entry.description,
                datetime.fromtimestamp(mktime(entry.updated_parsed)),
            )
            news.append(feed_entry)

        return tuple(news)

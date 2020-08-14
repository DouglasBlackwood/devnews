import warnings

from devnews.devnews import get_news
from devnews.entities import Article


def test_main():
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = get_news()

    assert len(news) > 0
    assert type(news[0]) == Article

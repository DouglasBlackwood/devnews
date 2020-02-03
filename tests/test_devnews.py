import warnings

from devnews import __version__
from devnews.devnews import get_news, FeedEntry


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = get_news()

    assert len(news) > 0
    assert type(news[0]) == FeedEntry

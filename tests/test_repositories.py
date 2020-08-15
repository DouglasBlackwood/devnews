import warnings

from devnews.entities import Article


def test_get_all(repo):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = repo.get_all()

    assert len(news) == 7
    assert type(news[0]) == Article

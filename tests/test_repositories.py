import warnings
from pathlib import Path

import pytest

from devnews.repositories import FeedNewsRepository

DATA_FILEPATH = Path(__file__).parent / "data"


@pytest.fixture
def repo():
    return FeedNewsRepository(DATA_FILEPATH)


def test_get_all(repo):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = repo.get_all()

    assert len(news) == 7

import pytest

from devnews.interfaces import NewsRepository


def test_abstract():
    with pytest.raises(TypeError, match="Can't instantiate abstract class NewsRepository with abstract methods get_all"):
        repo = NewsRepository()
        repo.get_all()

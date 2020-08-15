import pytest

from devnews.interfaces import NewsRepository


def test_abstract():
    error_string = (
        "Can't instantiate abstract class NewsRepository with abstract methods get_all"
    )
    with pytest.raises(TypeError, match=error_string):
        repo = NewsRepository()
        repo.get_all()

import warnings

import pytest

from devnews.use_cases import ListNewsUseCase


@pytest.fixture
def use_case():
    return ListNewsUseCase()


def test_setup(use_case):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = use_case.execute()
        assert news

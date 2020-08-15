from pathlib import Path

import pytest

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase, SearchNewsUseCase

DATA_FILEPATH = Path(__file__).parent / "data"


@pytest.fixture
def repo():
    return FeedNewsRepository(DATA_FILEPATH)


@pytest.fixture
def list_use_case(repo):
    return ListNewsUseCase(repo)


@pytest.fixture
def search_use_case(repo):
    return SearchNewsUseCase(repo)

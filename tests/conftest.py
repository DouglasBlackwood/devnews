from pathlib import Path

import pytest

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase

DATA_FILEPATH = Path(__file__).parent / "data"


@pytest.fixture
def repo():
    return FeedNewsRepository(DATA_FILEPATH)


@pytest.fixture
def use_case(repo):
    return ListNewsUseCase(repo)

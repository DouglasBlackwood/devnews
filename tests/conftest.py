from pathlib import Path

import pytest

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase, SearchNewsUseCase
import devnews.api

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


@pytest.fixture
def flask_app():
    # Patch la liste des URLS vers un fichier de test
    devnews.api.URLS = [DATA_FILEPATH]
    return devnews.api.create_app()


@pytest.fixture
def flask_client(flask_app):
    return flask_app.test_client()

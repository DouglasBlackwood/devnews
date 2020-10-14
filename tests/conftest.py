from pathlib import Path

import pytest

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase, SearchNewsUseCase
import devnews.api
import devnews.web

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
def api_app():
    # Patch la liste des URLS vers un fichier de test
    devnews.api.URLS = [DATA_FILEPATH]
    return devnews.api.create_app()


@pytest.fixture
def api_client(api_app):
    return api_app.test_client()


@pytest.fixture
def web_client():
    # Patch la liste des URLS vers un fichier de test
    devnews.web.URLS = [DATA_FILEPATH]
    return devnews.web.APP.test_client()

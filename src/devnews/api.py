import json
from pathlib import Path
from dataclasses import asdict

import connexion

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import SearchNewsUseCase

APP_DIR = Path(__file__).parent
CONFIG_DIR = APP_DIR / "config"

with open(CONFIG_DIR / 'urls.json') as json_file:
    URLS = json.load(json_file)


def create_app():
    app = connexion.App("Devnews", specification_dir=CONFIG_DIR)
    app.add_api("swagger.yaml")

    return app.app


def search_news(q=""):
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = SearchNewsUseCase(*repositories)
    news = use_case.execute(q)

    return {"news": [asdict(a) for a in news]}

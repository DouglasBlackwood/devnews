from pathlib import Path
from dataclasses import asdict

import connexion

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import SearchNewsUseCase

APP_DIR = Path(__file__).parent
CONFIG_DIR = APP_DIR / "config"

URLS = (
    "http://feeds.wired.com/wired/index",
    "http://hackaday.com/feed/",
    "http://news.ycombinator.com/rss",
    "http://rss.slashdot.org/Slashdot/slashdot",
    "http://feeds.dzone.com/home",
    "http://www.engadget.com/rss.xml",
    "http://www.reddit.com/r/gaming/.rss",
    "http://www.reddit.com/r/geek/.rss",
    "http://www.reddit.com/r/programming/.rss",
    "http://www.reddit.com/r/science/.rss",
    "http://www.reddit.com/r/scifi/.rss",
    "http://www.reddit.com/r/technology/.rss",
    "http://www.techmeme.com/index.xml",
)


def create_app():
    app = connexion.App("Devnews", specification_dir=CONFIG_DIR)
    app.add_api("swagger.yaml")

    return app.app


def search_news(q=""):
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = SearchNewsUseCase(*repositories)
    news = use_case.execute(q)

    return {"news": [asdict(a) for a in news]}

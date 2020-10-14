import json
from pathlib import Path

from flask import Flask, render_template

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import ListNewsUseCase

APP = Flask(__name__)

APP_DIR = Path(__file__).parent
CONFIG_DIR = APP_DIR / 'config'

with open(CONFIG_DIR / 'urls.json') as json_file:
    URLS = json.load(json_file)


@APP.route('/devnews/')
def hello_world():
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = ListNewsUseCase(*repositories)
    articles = use_case.execute()
    return render_template("devnews.html", articles=articles)

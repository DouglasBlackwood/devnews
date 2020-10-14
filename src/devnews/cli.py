import json
from pathlib import Path

import click
from terminaltables import SingleTable

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import SearchNewsUseCase

APP_DIR = Path(__file__).parent
CONFIG_DIR = APP_DIR / 'config'

with open(CONFIG_DIR / 'urls.json') as json_file:
    URLS = json.load(json_file)


@click.command(options_metavar="<options>")
@click.argument("query", nargs=-1, metavar="<query>")
def list_news(query):
    """ Recherche les dernières news

        <query> termes de recherche
    """
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = SearchNewsUseCase(*repositories)
    news = use_case.execute(query)

    data = [(article.source_name, article.wrapped_summary) for article in news[:10]]
    data.insert(0, ("Feed", "Title"))
    table = SingleTable(data)
    click.echo(table.table)


if __name__ == "__main__":
    list_news()

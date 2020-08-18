import click
from terminaltables import SingleTable

from devnews.repositories import FeedNewsRepository
from devnews.use_cases import SearchNewsUseCase

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


@click.command(options_metavar='<options>')
@click.argument("query", nargs=-1, metavar='<query>')
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


if __name__ == '__main__':
    list_news()

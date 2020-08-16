import click

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


@click.command()
@click.argument('query', nargs=-1)
def list_news(query):
    repositories = [FeedNewsRepository(url) for url in URLS]
    use_case = SearchNewsUseCase(*repositories)
    news = use_case.execute(query)

    for article in news[:5]:
        click.echo(article)


if __name__ == '__main__':
    list_news()

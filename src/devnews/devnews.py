import feedparser

URLS = (
    "http://news.ycombinator.com/rss",
    "http://hackaday.com/feed/",
    "http://rss.slashdot.org/Slashdot/slashdot",
    "http://www.dzone.com/links/feed/frontpage/rss.xml",
    "http://www.techmeme.com/index.xml",
    "http://feeds.wired.com/wired/index",
)


def main():
    for url in URLS:
        feedparser.parse(url)


if __name__ == "__main__":
    main()

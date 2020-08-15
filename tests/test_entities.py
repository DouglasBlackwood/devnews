from datetime import datetime

from devnews.entities import Article


def test_article():
    updated_at = datetime.now()
    datas = {
        "source_name": "Source",
        "title": "Title",
        "link": "http://example.com",
        "description": "This is a description",
        "updated_at": updated_at,
    }
    article = Article(**datas)

    assert article.source_name == "Source"
    assert article.title == "Title"
    assert article.link == "http://example.com"
    assert article.description == "This is a description"
    assert article.updated_at == updated_at

    expected_search_words = set(("source", "title", "this", "is", "a", "description"))
    assert article.search_words == expected_search_words
    assert article.contains(expected_search_words)

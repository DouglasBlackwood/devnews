import warnings


def test_web(web_client):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")
        response = web_client.get("/devnews/")

    assert response.status_code == 200

    assert b"<!doctype html>" in response.data
    assert b"<title>Devnews</title>" in response.data
    assert b"<h1>Devnews</h1>" in response.data
    assert b"<ul>" in response.data
    assert b"<li>Moving Fridge Magnets Make for Unique Clock</li>" in response.data

import warnings


def test_get(api_client):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        response = api_client.get("/api/devnews")

    assert response.status_code == 200
    assert "news" in response.json
    assert len(response.json["news"]) == 7

    first_article = response.json["news"][0]
    assert first_article["source_name"] == "Hackaday"
    assert first_article["title"] == "Moving Fridge Magnets Make for Unique Clock"


def test_get_with_query(api_client):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        response = api_client.get("/api/devnews?q=3d")

    assert response.status_code == 200
    assert "news" in response.json
    assert len(response.json["news"]) == 2

    first_article = response.json["news"][0]
    assert first_article["source_name"] == "Hackaday"
    assert (
        first_article["title"]
        == "Tensile Testing Machine Takes 3D Printed Parts to the Breaking Point"
    )


def test_get_with_query2(api_client):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        response = api_client.get("/api/devnews?q=3d+torque")

    assert response.status_code == 200
    assert "news" in response.json
    assert len(response.json["news"]) == 1

    first_article = response.json["news"][0]
    assert first_article["source_name"] == "Hackaday"
    assert (
        first_article["title"]
        == "A High Torque Gearbox You Can Print At Home"
    )

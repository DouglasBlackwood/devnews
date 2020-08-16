import warnings


def test_list_use_case(list_use_case):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = list_use_case.execute()
        assert len(news) == 7

        expected_order = tuple(sorted(news, key=lambda a: a.updated_at, reverse=True))
        assert news == expected_order


def test_search_use_case(search_use_case):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = search_use_case.execute(q="3d")
        assert len(news) == 2


def test_search_use_case_with_two_words(search_use_case):
    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        news = search_use_case.execute(q="3d torque")
        assert len(news) == 1
        assert news[0].title == "A High Torque Gearbox You Can Print At Home"

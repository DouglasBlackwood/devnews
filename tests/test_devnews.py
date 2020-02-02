from devnews import __version__
from devnews.devnews import main


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    main()

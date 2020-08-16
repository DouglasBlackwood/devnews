import warnings
from pathlib import Path

from click.testing import CliRunner

import devnews.cli

DATA_FILEPATH = Path(__file__).parent / "data"


def test_list_news():
    # Patch la liste des URLS vers un fichier de test
    devnews.cli.URLS = [DATA_FILEPATH]

    with warnings.catch_warnings():
        # Désactive temporairement les DeprecationWarnings émit par la lib
        # tierce feedparser
        warnings.simplefilter("ignore")

        runner = CliRunner()
        result = runner.invoke(devnews.cli.list_news)

    assert result.exit_code == 0

    lines = result.output.split("\n")
    assert len(lines) == 12
    assert "Feed" in lines[1]
    assert "Title" in lines[1]
    assert "Hackaday" in lines[3]
    assert "Moving Fridge Magnets Make for Unique Clock" in lines[3]

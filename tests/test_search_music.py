# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search.music.models import SearchMusicModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("CASANOVA POSSE", id="casanova posse music")]


# TODO: Validate
class SearchMusicTest(RecordedEndpoint):
    MODEL = SearchMusicModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    SearchMusicTest.download_test(query, lambda: client.search_music.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(query: str) -> None:
    SearchMusicTest.parse_test(query)

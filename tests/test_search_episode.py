# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search.episode.models import SearchEpisodeModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("This Is #COMPASS2.0", id="compass 2.0 episode")]


# TODO: Validate
class SearchEpisodeTest(RecordedEndpoint):
    MODEL = SearchEpisodeModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    SearchEpisodeTest.download_test(
        query,
        lambda: client.search_episode.download(query),
    )


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(query: str) -> None:
    SearchEpisodeTest.parse_test(query)

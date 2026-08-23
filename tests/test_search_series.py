# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search.series.models import SearchSeriesModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("#COMPASS2.0 ANIMATION PROJECT", id="compass 2.0 series")]


# TODO: Validate
class SearchSeriesTest(RecordedEndpoint):
    MODEL = SearchSeriesModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    SearchSeriesTest.download_test(query, lambda: client.search_series.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(query: str) -> None:
    SearchSeriesTest.parse_test(query)

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search.movie_listing.models import SearchMovieListingModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [
    pytest.param("009-1: The End of the Beginning", id="009-1 movie listing"),
]


# TODO: Validate
class SearchMovieListingTest(RecordedEndpoint):
    MODEL = SearchMovieListingModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    SearchMovieListingTest.download_test(
        query,
        lambda: client.search_movie_listing.download(query),
    )


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(query: str) -> None:
    SearchMovieListingTest.parse_test(query)

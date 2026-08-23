# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search import Search
from chirashi.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from collections.abc import Callable

    from chirashi import Chirashi
    from chirashi.search.models import Item

QUERIES = [
    pytest.param("#COMPASS2.0 ANIMATION PROJECT", id="compass 2.0 series"),
    pytest.param("This Is #COMPASS2.0", id="compass 2.0 episode"),
    pytest.param("CASANOVA POSSE", id="casanova posse music"),
    pytest.param("009-1: The End of the Beginning", id="009-1 movie listing"),
]


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(query: str) -> None:
    SearchTest.parse_test(query)


# TODO: Validate
@pytest.mark.parametrize(
    ("query", "extract"),
    [
        pytest.param(
            "#COMPASS2.0 ANIMATION PROJECT",
            Search.extract_top_results,
            id="top results",
        ),
        pytest.param(
            "#COMPASS2.0 ANIMATION PROJECT",
            Search.extract_series,
            id="series",
        ),
        pytest.param("This Is #COMPASS2.0", Search.extract_episode, id="episode"),
        pytest.param("CASANOVA POSSE", Search.extract_music, id="music"),
        pytest.param(
            "009-1: The End of the Beginning",
            Search.extract_movie_listing,
            id="movie listing",
        ),
    ],
)
def test_extract(
    client: Chirashi,
    query: str,
    extract: Callable[[Search, SearchModel], list[Item]],
) -> None:
    results = extract(
        client.search,
        client.search.load(SearchTest.recorded_content(query)),
    )
    # Ads are sometimes injected directly into search results.
    assert query in [result.title for result in results]

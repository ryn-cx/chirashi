# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search import Search

if TYPE_CHECKING:
    from collections.abc import Callable

    from chirashi import Chirashi
    from chirashi.search.models import Item, SearchModel

QUERIES = [
    pytest.param(
        "#COMPASS2.0 ANIMATION PROJECT",
        Search.extract_top_results,
        id="top results",
    ),
    pytest.param("#COMPASS2.0 ANIMATION PROJECT", Search.extract_series, id="series"),
    pytest.param("This Is #COMPASS2.0", Search.extract_episode, id="episode"),
    pytest.param("CASANOVA POSSE", Search.extract_music, id="music"),
    pytest.param(
        "009-1: The End of the Beginning",
        Search.extract_movie_listing,
        id="movie listing",
    ),
]


# TODO: Validate
@pytest.mark.parametrize(("query", "extract"), QUERIES)
def test_download(
    client: Chirashi,
    query: str,
    extract: Callable[[Search, SearchModel], list[Item]],
) -> None:
    results = extract(client.search, client.search(query))
    assert query in [result.title for result in results]

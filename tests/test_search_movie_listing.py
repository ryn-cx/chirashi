# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("009-1: The End of the Beginning", id="009-1 movie listing")]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    results = client.search_movie_listing(query)
    assert results.type == "movie_listing"
    assert query in [item.title for item in results.items]

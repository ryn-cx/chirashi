# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("This Is #COMPASS2.0", id="compass 2.0 episode")]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    results = client.search_episode(query)
    assert results.type == "episode"
    assert query in [item.title for item in results.items]

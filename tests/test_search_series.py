# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("#COMPASS2.0 ANIMATION PROJECT", id="compass 2.0 series")]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    results = client.search_series(query)
    assert results.type == "series"
    assert query in [item.title for item in results.items]

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

QUERIES = [pytest.param("CASANOVA POSSE", id="casanova posse music")]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Chirashi, query: str) -> None:
    results = client.search_music(query)
    assert results.type == "music"
    assert query in [item.title for item in results.items]

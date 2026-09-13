# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GG5H5XQX4", id="frieren: beyond journey's end")]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    categories = client.categories(series_id)
    assert categories.total == len(categories.data)
    assert all(category.id for category in categories.data)


# TODO: Validate
def test_download_without_categories(client: Chirashi) -> None:
    categories = client.categories("GGGGGGGGG")
    assert categories.total == 0
    assert categories.data == []

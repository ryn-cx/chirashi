# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GEXH3W29Z", id="#compass2.0 animation project")]
SERIES_IDS_WITHOUT_SEASONS = [
    pytest.param("GGGGGGGGG", id="Series that does not exist"),
    pytest.param("G1XHJVW55", id="Series without seasons"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    seasons = client.seasons(series_id)
    assert seasons.total == len(seasons.data)
    assert all(season.series_id == series_id for season in seasons.data)


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS_WITHOUT_SEASONS)
def test_download_without_seasons(client: Chirashi, series_id: str) -> None:
    seasons = client.seasons(series_id)
    assert seasons.total == 0
    assert seasons.data == []

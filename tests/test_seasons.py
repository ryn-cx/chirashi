# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GEXH3W29Z", id="#compass2.0 animation project")]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    seasons = client.seasons(series_id)
    assert seasons.total == len(seasons.data)
    assert all(season.series_id == series_id for season in seasons.data)


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.seasons.download("GGGGGGGGG")

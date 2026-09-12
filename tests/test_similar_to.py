# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GR751KNZY", id="Attack on Titan")]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    similar_to = client.similar_to(series_id)
    assert similar_to.data
    assert len(similar_to.data) <= similar_to.total


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    similar_to = client.similar_to("GGGGGGGGG")
    assert similar_to.total == 0
    assert similar_to.data == []

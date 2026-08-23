# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeriesNotFoundError
from chirashi.seasons.models import SeasonsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GEXH3W29Z", id="#compass2.0 animation project")]


# TODO: Validate
class SeasonsTest(RecordedEndpoint):
    MODEL = SeasonsModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    SeasonsTest.download_test(series_id, lambda: client.seasons.download(series_id))


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(series_id: str) -> None:
    SeasonsTest.parse_test(series_id)


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param("GGGGGGGGG", id="series that does not exist")],
)
def test_download_invalid(client: Chirashi, series_id: str) -> None:
    SeasonsTest.error_test(
        series_id,
        lambda: client.seasons.download(series_id),
        SeriesNotFoundError,
    )

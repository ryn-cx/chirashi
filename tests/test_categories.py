# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.categories.models import CategoriesModel
from chirashi.exceptions import SeriesNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

SERIES_IDS = [pytest.param("GG5H5XQX4", id="frieren: beyond journey's end")]


# TODO: Validate
class CategoriesTest(RecordedEndpoint):
    MODEL = CategoriesModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: Chirashi, series_id: str) -> None:
    CategoriesTest.download_test(
        series_id,
        lambda: client.categories.download(series_id),
    )


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(series_id: str) -> None:
    CategoriesTest.parse_test(series_id)


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param("GGGGGGGGG", id="series that does not exist")],
)
def test_download_invalid(client: Chirashi, series_id: str) -> None:
    CategoriesTest.error_test(
        series_id,
        lambda: client.categories.download(series_id),
        SeriesNotFoundError,
    )

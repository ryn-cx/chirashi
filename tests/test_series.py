# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.series import Series
    from chirashi.series.models import SeriesModel

SERIES_ID = "GG5H5XQX4"
INVALID_SERIES_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Series:
    return client.series


@pytest.fixture(scope="session")
def json_file(endpoint: Series) -> Path:
    return data_path(endpoint, SERIES_ID)


@pytest.fixture(scope="session")
def data(endpoint: Series, json_file: Path) -> SeriesModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSeries:
    def test_download(self, endpoint: Series) -> None:
        download_if_missing(
            endpoint,
            SERIES_ID,
            lambda: endpoint.download(SERIES_ID),
        )

    def test_value(self, data: SeriesModel) -> None:
        # TODO: assert the series id matches SERIES_ID (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: Series) -> None:
        assert_http_error(
            endpoint,
            INVALID_SERIES_ID,
            lambda: endpoint.download(INVALID_SERIES_ID),
        )

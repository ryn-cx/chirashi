# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.constants import INVALID_SEARCH_QUERY
from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.search.series import SearchSeries
    from chirashi.search.series.models import SearchSeriesModel

QUERY = "#COMPASS2.0 ANIMATION PROJECT"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchSeries:
    return client.search.series


@pytest.fixture(scope="session")
def json_file(endpoint: SearchSeries) -> Path:
    return data_path(endpoint, QUERY)


@pytest.fixture(scope="session")
def data(endpoint: SearchSeries, json_file: Path) -> SearchSeriesModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSearchSeries:
    def test_download(self, endpoint: SearchSeries) -> None:
        download_if_missing(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_value(self, data: SearchSeriesModel) -> None:
        # TODO: assert the expected series id is present (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: SearchSeries) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.get(INVALID_SEARCH_QUERY),
        )

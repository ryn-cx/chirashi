# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.browse_series import Browse
    from chirashi.browse_series.models import BrowseSeriesModel

START = 0
ENTRIES_PER_PAGE = 36


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Browse:
    return client.browse_series


@pytest.fixture(scope="session")
def json_file(endpoint: Browse) -> Path:
    return data_path(endpoint, str(START))


@pytest.fixture(scope="session")
def data(endpoint: Browse, json_file: Path) -> BrowseSeriesModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestBrowseSeries:
    def test_download(self, endpoint: Browse) -> None:
        download_if_missing(
            endpoint,
            str(START),
            lambda: endpoint.download(start=START),
        )

    def test_value(self, data: BrowseSeriesModel) -> None:
        # TODO: assert the total and per-page entry counts (needs live data)
        assert data.data is not None

    def test_compile_entries_from_single_browse(
        self,
        endpoint: Browse,
        data: BrowseSeriesModel,
    ) -> None:
        entries = endpoint.compile_entries(data)
        assert entries == data.data

    def test_compile_entries_from_list_of_browses(
        self,
        endpoint: Browse,
        data: BrowseSeriesModel,
    ) -> None:
        models = [data]
        entries = endpoint.compile_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected

    def test_past_last_page(self, endpoint: Browse) -> None:
        first_page = endpoint.get()
        last_page_entries = first_page.total % ENTRIES_PER_PAGE or ENTRIES_PER_PAGE
        start = first_page.total - last_page_entries + ENTRIES_PER_PAGE
        assert_no_content_error(
            endpoint,
            "past_last_page",
            lambda: endpoint.get(start=start),
        )

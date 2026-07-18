# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.series import SearchSeries

QUERY = "#COMPASS2.0 ANIMATION PROJECT"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchSeries:
    return client.search.series


class TestSearchSeries:
    def test_download(self, endpoint: SearchSeries) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchSeries) -> None:
        # TODO: assert the expected series id is present (needs live data)
        data = parse_json(endpoint, QUERY)
        assert data.data is not None

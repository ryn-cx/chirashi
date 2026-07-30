from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.series import SearchSeries

QUERY = "#COMPASS2.0 ANIMATION PROJECT"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> SearchSeries:
    return client.search_series


def test_download(client: SearchSeries) -> None:
    download_and_save(client, QUERY, lambda: client.download(QUERY))


def test_parse(client: SearchSeries) -> None:
    data = parsed_json(client, QUERY)
    # Ads are sometimes injected directly into search results.
    assert QUERY in [item.title for item in data.data[0].items]

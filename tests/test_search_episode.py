# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.episode import SearchEpisode

QUERY = "This Is #COMPASS2.0"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchEpisode:
    return client.search.episode


class TestSearchEpisode:
    def test_download(self, endpoint: SearchEpisode) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchEpisode) -> None:
        # TODO: assert the expected episode id and type are present (needs live
        # data)
        data = parse_json(endpoint, QUERY)
        assert data.data is not None

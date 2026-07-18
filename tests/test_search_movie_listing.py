# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.movie_listing import SearchMovieListing

QUERY = "009-1: The End of the Beginning"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMovieListing:
    return client.search.movie_listing


class TestSearchMovieListing:
    def test_download(self, endpoint: SearchMovieListing) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchMovieListing) -> None:
        # TODO: assert the expected movie listing id and type are present
        # (needs live data)
        data = parse_json(endpoint, QUERY)
        assert data.data is not None

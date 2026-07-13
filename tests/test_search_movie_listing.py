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
    from chirashi.search.movie_listing import SearchMovieListing
    from chirashi.search.movie_listing.models import SearchMovieListingModel

QUERY = "009-1: The End of the Beginning"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMovieListing:
    return client.search.movie_listing


@pytest.fixture(scope="session")
def json_file(endpoint: SearchMovieListing) -> Path:
    return data_path(endpoint, QUERY)


@pytest.fixture(scope="session")
def data(endpoint: SearchMovieListing, json_file: Path) -> SearchMovieListingModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSearchMovieListing:
    def test_download(self, endpoint: SearchMovieListing) -> None:
        download_if_missing(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_value(self, data: SearchMovieListingModel) -> None:
        # TODO: assert the expected movie listing id and type are present
        # (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: SearchMovieListing) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.get(INVALID_SEARCH_QUERY),
        )

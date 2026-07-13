# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.search.episode.models import Item as EpisodeItem
from chirashi.search.models import Item as TopResultItem
from chirashi.search.movie_listing.models import Item as MovieListingItem
from chirashi.search.music.models import Item as MusicItem
from chirashi.search.series.models import Item as SeriesItem
from tests.constants import INVALID_SEARCH_QUERY
from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.search import Search
    from chirashi.search.models import SearchModel

QUERY = "#COMPASS2.0 ANIMATION PROJECT"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Search:
    return client.search


@pytest.fixture(scope="session")
def json_file(endpoint: Search) -> Path:
    return data_path(endpoint, QUERY)


@pytest.fixture(scope="session")
def data(endpoint: Search, json_file: Path) -> SearchModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSearch:
    def test_download(self, endpoint: Search) -> None:
        download_if_missing(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_extract_top_results(self, endpoint: Search, data: SearchModel) -> None:
        results = endpoint.extract_top_results(data)
        assert all(isinstance(item, TopResultItem) for item in results)

    def test_extract_series(self, endpoint: Search, data: SearchModel) -> None:
        results = endpoint.extract_series(data)
        assert all(isinstance(item, SeriesItem) for item in results)
        # TODO: assert the expected series id is present (needs live data)

    def test_extract_episode(self, endpoint: Search, data: SearchModel) -> None:
        results = endpoint.extract_episode(data)
        assert all(isinstance(item, EpisodeItem) for item in results)

    def test_extract_music(self, endpoint: Search, data: SearchModel) -> None:
        results = endpoint.extract_music(data)
        assert all(isinstance(item, MusicItem) for item in results)

    def test_extract_movie_listing(self, endpoint: Search, data: SearchModel) -> None:
        results = endpoint.extract_movie_listing(data)
        assert all(isinstance(item, MovieListingItem) for item in results)

    def test_invalid(self, endpoint: Search) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.get(INVALID_SEARCH_QUERY),
        )

# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError
from chirashi.search.episode.models import Item as EpisodeItem
from chirashi.search.models import Item as TopResultItem
from chirashi.search.movie_listing.models import Item as MovieListingItem
from chirashi.search.music.models import Item as MusicItem
from chirashi.search.series.models import Item as SeriesItem
from tests.constants import INVALID_SEARCH_QUERY

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search import Search


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Search:
    return client.search


class TestSearch:
    def test_get(self, endpoint: Search) -> None:
        model = endpoint.get("#COMPASS2.0 ANIMATION PROJECT")
        series_results = endpoint.extract_series(model)
        assert any(series.id == "GEXH3W29Z" for series in series_results)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: Search) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_top_results(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            results = endpoint.extract_top_results(model)
            assert all(isinstance(item, TopResultItem) for item in results)

    def test_extract_series(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            results = endpoint.extract_series(model)
            assert all(isinstance(item, SeriesItem) for item in results)

    def test_extract_episode(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            results = endpoint.extract_episode(model)
            assert all(isinstance(item, EpisodeItem) for item in results)

    def test_extract_music(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            results = endpoint.extract_music(model)
            assert all(isinstance(item, MusicItem) for item in results)

    def test_extract_movie_listing(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            results = endpoint.extract_movie_listing(model)
            assert all(isinstance(item, MovieListingItem) for item in results)

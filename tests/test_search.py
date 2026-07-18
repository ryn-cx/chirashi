# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.search.episode.models import Item as EpisodeItem
from chirashi.search.models import Item as TopResultItem
from chirashi.search.movie_listing.models import Item as MovieListingItem
from chirashi.search.music.models import Item as MusicItem
from chirashi.search.series.models import Item as SeriesItem
from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search import Search

QUERY = "#COMPASS2.0 ANIMATION PROJECT"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Search:
    return client.search


class TestSearch:
    def test_download(self, endpoint: Search) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_extract_top_results(self, endpoint: Search) -> None:
        results = endpoint.extract_top_results(parse_json(endpoint, QUERY))
        assert all(isinstance(item, TopResultItem) for item in results)

    def test_extract_series(self, endpoint: Search) -> None:
        # TODO: assert the expected series id is present (needs live data)
        results = endpoint.extract_series(parse_json(endpoint, QUERY))
        assert all(isinstance(item, SeriesItem) for item in results)

    def test_extract_episode(self, endpoint: Search) -> None:
        results = endpoint.extract_episode(parse_json(endpoint, QUERY))
        assert all(isinstance(item, EpisodeItem) for item in results)

    def test_extract_music(self, endpoint: Search) -> None:
        results = endpoint.extract_music(parse_json(endpoint, QUERY))
        assert all(isinstance(item, MusicItem) for item in results)

    def test_extract_movie_listing(self, endpoint: Search) -> None:
        results = endpoint.extract_movie_listing(parse_json(endpoint, QUERY))
        assert all(isinstance(item, MovieListingItem) for item in results)


@pytest.mark.parametrize("n", [6, 12])
def test_log_id(endpoint: Search, n: int) -> None:
    expected = f"Search q={QUERY!r}"
    if n != 6:  # noqa: PLR2004
        expected += f" n={n!r}"
    assert endpoint.get_log_id(QUERY, n=n) == expected

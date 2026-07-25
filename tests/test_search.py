from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search import Search

TOP_RESULTS_QUERY = "#COMPASS2.0 ANIMATION PROJECT"
SERIES_QUERY = "#COMPASS2.0 ANIMATION PROJECT"
EPISODE_QUERY = "This Is #COMPASS2.0"
MUSIC_QUERY = "CASANOVA POSSE"
MOVIE_LISTING_QUERY = "009-1: The End of the Beginning"

QUERIES = [
    TOP_RESULTS_QUERY,
    EPISODE_QUERY,
    MUSIC_QUERY,
    MOVIE_LISTING_QUERY,
]


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Search:
    return client.search


@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Search, query: str) -> None:
    download_and_save(client, query, lambda: client.download(query))


def test_extract_top_results(client: Search) -> None:
    results = client.extract_top_results(parsed_json(client, TOP_RESULTS_QUERY))
    assert results[0].title == TOP_RESULTS_QUERY


def test_extract_series(client: Search) -> None:
    results = client.extract_series(parsed_json(client, SERIES_QUERY))
    assert results[0].title == SERIES_QUERY


def test_extract_episode(client: Search) -> None:
    results = client.extract_episode(parsed_json(client, EPISODE_QUERY))
    assert results[0].title == EPISODE_QUERY


def test_extract_music(client: Search) -> None:
    results = client.extract_music(parsed_json(client, MUSIC_QUERY))
    assert results[0].title == MUSIC_QUERY


def test_extract_movie_listing(client: Search) -> None:
    results = client.extract_movie_listing(parsed_json(client, MOVIE_LISTING_QUERY))
    assert results[0].title == MOVIE_LISTING_QUERY

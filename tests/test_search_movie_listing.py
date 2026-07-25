from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.movie_listing import SearchMovieListing

QUERY = "009-1: The End of the Beginning"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> SearchMovieListing:
    return client.search_movie_listing


def test_download(client: SearchMovieListing) -> None:
    download_and_save(client, QUERY, lambda: client.download(QUERY))


def test_parse(client: SearchMovieListing) -> None:
    data = parsed_json(client, QUERY)
    assert data.data[0].items[0].title == QUERY

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.episode import SearchEpisode

QUERY = "This Is #COMPASS2.0"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> SearchEpisode:
    return client.search_episode


def test_download(client: SearchEpisode) -> None:
    download_and_save(client, QUERY, lambda: client.download(QUERY))


def test_parse(client: SearchEpisode) -> None:
    data = parsed_json(client, QUERY)
    assert data.data[0].items[0].title == QUERY

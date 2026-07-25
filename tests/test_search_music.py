from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.music import SearchMusic

QUERY = "CASANOVA POSSE"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> SearchMusic:
    return client.search_music


def test_download(client: SearchMusic) -> None:
    download_and_save(client, QUERY, lambda: client.download(QUERY))


def test_parse(client: SearchMusic) -> None:
    data = parsed_json(client, QUERY)
    assert data.data[0].items[0].title == QUERY

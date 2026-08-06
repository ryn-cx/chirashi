from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ArtistNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.artist import Artist

# https://www.crunchyroll.com/artist/MA36EDC261/ali
ARTIST_ID = "MA36EDC261"
INVALID_ARTIST_ID = "MA00000000"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Artist:
    return client.artist


def test_download(client: Artist) -> None:
    download_and_save(client, ARTIST_ID, lambda: client.download(ARTIST_ID))


def test_parse(client: Artist) -> None:
    data = parsed_json(client, ARTIST_ID)
    assert data.data[0].id == ARTIST_ID


def test_download_invalid(client: Artist) -> None:
    assert_error(
        client,
        INVALID_ARTIST_ID,
        lambda: client.download(INVALID_ARTIST_ID),
        ArtistNotFoundError,
    )

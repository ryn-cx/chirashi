from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ArtistNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.artist_concerts import ArtistConcerts

# https://www.crunchyroll.com/artist/MA6480DAB5/shoko-nakagawa
ARTIST_ID = "MA6480DAB5"
# https://www.crunchyroll.com/artist/MA36EDC261/ali
ARTIST_ID_WITHOUT_CONCERTS = "MA36EDC261"
INVALID_ARTIST_ID = "MA00000000"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> ArtistConcerts:
    return client.artist_concerts


def test_download(client: ArtistConcerts) -> None:
    download_and_save(client, ARTIST_ID, lambda: client.download(ARTIST_ID))


def test_download_without_concerts(client: ArtistConcerts) -> None:
    download_and_save(
        client,
        ARTIST_ID_WITHOUT_CONCERTS,
        lambda: client.download(ARTIST_ID_WITHOUT_CONCERTS),
    )


def test_parse(client: ArtistConcerts) -> None:
    data = parsed_json(client, ARTIST_ID)
    assert data.total == len(data.data)


def test_parse_without_concerts(client: ArtistConcerts) -> None:
    data = parsed_json(client, ARTIST_ID_WITHOUT_CONCERTS)
    assert data.total == 0
    assert data.data == []


def test_download_invalid(client: ArtistConcerts) -> None:
    assert_error(
        client,
        INVALID_ARTIST_ID,
        lambda: client.download(INVALID_ARTIST_ID),
        ArtistNotFoundError,
    )

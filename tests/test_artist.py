# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.artist import Artist
from chirashi.artist.models import ArtistModel
from chirashi.exceptions import ArtistNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

ARTIST_IDS = [
    # https://www.crunchyroll.com/artist/MA36EDC261/ali
    pytest.param("MA36EDC261", id="ali"),
]


# TODO: Validate
class ArtistTest(RecordedEndpoint):
    MODEL = ArtistModel


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_download(client: Chirashi, artist_id: str) -> None:
    ArtistTest.download_test(artist_id, lambda: client.artist.download(artist_id))


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_parse(artist_id: str) -> None:
    ArtistTest.parse_test(artist_id)


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_lookup(
    client: Chirashi,
    monkeypatch: pytest.MonkeyPatch,
    artist_id: str,
) -> None:
    """`Chirashi.artist(id)` downloads and loads in one call."""
    recorded = ArtistTest.recorded_content(artist_id)
    # Chirashi.artist goes through the endpoint, so that is what is stubbed.
    monkeypatch.setattr(Artist, "download", lambda *_args, **_kwargs: recorded)

    assert client.artist(artist_id).data[0].id == artist_id


# TODO: Validate
@pytest.mark.parametrize(
    "artist_id",
    [pytest.param("MA00000000", id="artist that does not exist")],
)
def test_download_invalid(client: Chirashi, artist_id: str) -> None:
    ArtistTest.error_test(
        artist_id,
        lambda: client.artist.download(artist_id),
        ArtistNotFoundError,
    )

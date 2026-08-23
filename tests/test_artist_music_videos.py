# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.artist_music_videos.models import ArtistMusicVideosModel
from chirashi.exceptions import ArtistNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

ARTIST_IDS = [
    # https://www.crunchyroll.com/artist/MA36EDC261/ali
    pytest.param("MA36EDC261", id="ali"),
]


# TODO: Validate
class ArtistMusicVideosTest(RecordedEndpoint):
    MODEL = ArtistMusicVideosModel


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_download(client: Chirashi, artist_id: str) -> None:
    ArtistMusicVideosTest.download_test(
        artist_id,
        lambda: client.artist_music_videos.download(artist_id),
    )


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_parse(artist_id: str) -> None:
    ArtistMusicVideosTest.parse_test(artist_id)


# TODO: Validate
@pytest.mark.parametrize(
    "artist_id",
    [pytest.param("MA00000000", id="artist that does not exist")],
)
def test_download_invalid(client: Chirashi, artist_id: str) -> None:
    ArtistMusicVideosTest.error_test(
        artist_id,
        lambda: client.artist_music_videos.download(artist_id),
        ArtistNotFoundError,
    )

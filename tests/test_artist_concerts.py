# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.artist_concerts.models import ArtistConcertsModel
from chirashi.exceptions import ArtistNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

ARTIST_IDS = [
    pytest.param("MA6480DAB5", id="shoko nakagawa"),
    pytest.param("MA36EDC261", id="ali, who has no concerts"),
]


# TODO: Validate
class ArtistConcertsTest(RecordedEndpoint):
    MODEL = ArtistConcertsModel


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_download(client: Chirashi, artist_id: str) -> None:
    ArtistConcertsTest.download_test(
        artist_id,
        lambda: client.artist_concerts.download(artist_id),
    )


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_parse(artist_id: str) -> None:
    ArtistConcertsTest.parse_test(artist_id)


# TODO: Validate
@pytest.mark.parametrize(
    "artist_id",
    [pytest.param("MA00000000", id="artist that does not exist")],
)
def test_download_invalid(client: Chirashi, artist_id: str) -> None:
    ArtistConcertsTest.error_test(
        artist_id,
        lambda: client.artist_concerts.download(artist_id),
        ArtistNotFoundError,
    )

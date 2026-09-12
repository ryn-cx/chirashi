# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ArtistNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

ARTISTS = [
    pytest.param("MA6480DAB5", 1, id="shoko nakagawa"),
    pytest.param("MA36EDC261", 0, id="ali, who has no concerts"),
]


# TODO: Validate
@pytest.mark.parametrize(("artist_id", "least_concerts"), ARTISTS)
def test_download(client: Chirashi, artist_id: str, least_concerts: int) -> None:
    concerts = client.artist_concerts(artist_id)
    assert concerts.total == len(concerts.data)
    assert concerts.total >= least_concerts


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(ArtistNotFoundError):
        client.artist_concerts.download("MA00000000")

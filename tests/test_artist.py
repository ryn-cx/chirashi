# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ArtistNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

# https://www.crunchyroll.com/artist/MA36EDC261/ali
ARTIST_IDS = [pytest.param("MA36EDC261", id="ali")]


# TODO: Validate
@pytest.mark.parametrize("artist_id", ARTIST_IDS)
def test_download(client: Chirashi, artist_id: str) -> None:
    artist = client.artist(artist_id)
    assert artist.id == artist_id
    assert artist.name


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(ArtistNotFoundError):
        client.artist.download("MA00000000")

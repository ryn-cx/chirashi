# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ConcertNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

# https://www.crunchyroll.com/watch/concert/MC51D55EA6
CONCERT_IDS = [
    pytest.param("MC51D55EA6", id="shoko nakagawa first concert - donyoku matsuri"),
]


# TODO: Validate
@pytest.mark.parametrize("concert_id", CONCERT_IDS)
def test_download(client: Chirashi, concert_id: str) -> None:
    concert = client.concert(concert_id)
    assert concert.id == concert_id
    assert concert.title


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(ConcertNotFoundError):
        client.concert.download("MC00000000")

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.concert.models import ConcertModel
from chirashi.exceptions import ConcertNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

CONCERT_IDS = [
    # https://www.crunchyroll.com/watch/concert/MC51D55EA6
    pytest.param("MC51D55EA6", id="shoko nakagawa first concert - donyoku matsuri"),
]


# TODO: Validate
class ConcertTest(RecordedEndpoint):
    MODEL = ConcertModel


# TODO: Validate
@pytest.mark.parametrize("concert_id", CONCERT_IDS)
def test_download(client: Chirashi, concert_id: str) -> None:
    ConcertTest.download_test(concert_id, lambda: client.concert.download(concert_id))


# TODO: Validate
@pytest.mark.parametrize("concert_id", CONCERT_IDS)
def test_parse(concert_id: str) -> None:
    ConcertTest.parse_test(concert_id)


# TODO: Validate
@pytest.mark.parametrize(
    "concert_id",
    [pytest.param("MC00000000", id="concert that does not exist")],
)
def test_download_invalid(client: Chirashi, concert_id: str) -> None:
    ConcertTest.error_test(
        concert_id,
        lambda: client.concert.download(concert_id),
        ConcertNotFoundError,
    )

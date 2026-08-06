from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import ConcertNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.concert import Concert

# https://www.crunchyroll.com/watch/concert/MC51D55EA6
CONCERT_ID = "MC51D55EA6"
INVALID_CONCERT_ID = "MC00000000"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Concert:
    return client.concert


def test_download(client: Concert) -> None:
    download_and_save(client, CONCERT_ID, lambda: client.download(CONCERT_ID))


def test_parse(client: Concert) -> None:
    data = parsed_json(client, CONCERT_ID)
    assert data.data[0].id == CONCERT_ID


def test_download_invalid(client: Concert) -> None:
    assert_error(
        client,
        INVALID_CONCERT_ID,
        lambda: client.download(INVALID_CONCERT_ID),
        ConcertNotFoundError,
    )

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeriesNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.seasons import Seasons

SERIES_ID = "GEXH3W29Z"
INVALID_SERIES_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Seasons:
    return client.seasons


def test_download(client: Seasons) -> None:
    download_and_save(client, SERIES_ID, lambda: client.download(SERIES_ID))


def test_parse(client: Seasons) -> None:
    data = parsed_json(client, SERIES_ID)
    assert data.data
    assert all(season.series_id == SERIES_ID for season in data.data)


def test_download_invalid(client: Seasons) -> None:
    assert_error(
        client,
        INVALID_SERIES_ID,
        lambda: client.download(INVALID_SERIES_ID),
        SeriesNotFoundError,
    )

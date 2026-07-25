from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeriesNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.series import Series

SERIES_ID = "GG5H5XQX4"
INVALID_SERIES_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Series:
    return client.series


def test_download(client: Series) -> None:
    download_and_save(client, SERIES_ID, lambda: client.download(SERIES_ID))


def test_parse(client: Series) -> None:
    data = parsed_json(client, SERIES_ID)
    assert data.data[0].id == SERIES_ID


def test_download_invalid(client: Series) -> None:
    assert_error(
        client,
        INVALID_SERIES_ID,
        lambda: client.download(INVALID_SERIES_ID),
        SeriesNotFoundError,
    )

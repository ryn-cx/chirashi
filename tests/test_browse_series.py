from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from chirashi.browse_series import N
from chirashi.exceptions import StartOutOfRangeError
from tests.utils import assert_error, download_and_save, loaded_json, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.browse_series import Browse


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Browse:
    return client.browse_series


def test_download(client: Browse) -> None:
    download_and_save(client, 0, lambda: client.download(start=0))


def test_download_until_datetime(client: Browse) -> None:
    end_datetime = datetime.now().astimezone() - timedelta(days=7)
    download_and_save(
        client,
        "until_datetime",
        lambda: client.download_until_datetime(end_datetime),
        "Multipage",
    )


def test_download_invalid(client: Browse) -> None:
    assert_error(
        client,
        9999,
        lambda: client.download(start=9999),
        StartOutOfRangeError,
    )


def test_parse(client: Browse) -> None:
    data = parsed_json(client, 0)
    assert len(data.data) == N


def test_parse_until_datetime(client: Browse) -> None:
    results = parsed_json(client, "until_datetime", category="Multipage")
    assert len(results) > 1
    for result in results:
        assert len(result.data) == N


def test_extract_data(client: Browse) -> None:
    loaded = loaded_json(client, 0)
    extracted_loaded = client.extract_data(loaded)

    data = parsed_json(client, 0)
    extracted_data = client.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == N


def test_extract_data_until_datetime(client: Browse) -> None:
    loaded = loaded_json(client, "until_datetime", category="Multipage")
    extracted_loaded = client.extract_data(loaded)

    data = parsed_json(client, "until_datetime", category="Multipage")
    extracted_data = client.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == len(loaded) * N

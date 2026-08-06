# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.browse_music import N
from chirashi.exceptions import StartOutOfRangeError
from tests.utils import assert_error, download_and_save, loaded_json, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.browse_music import BrowseMusic

# The catalogue is a few hundred artists, so a start this far out is always past
# the end of it.
OUT_OF_RANGE_START = 9999


@pytest.fixture(scope="session")
def client(client: Chirashi) -> BrowseMusic:
    return client.browse_music


def test_download(client: BrowseMusic) -> None:
    download_and_save(client, 0, lambda: client.download(start=0))


def test_download_all(client: BrowseMusic) -> None:
    download_and_save(client, "all", client.download_all, "Multipage")


def test_download_invalid(client: BrowseMusic) -> None:
    assert_error(
        client,
        OUT_OF_RANGE_START,
        lambda: client.download(start=OUT_OF_RANGE_START),
        StartOutOfRangeError,
    )


def test_parse(client: BrowseMusic) -> None:
    data = parsed_json(client, 0)
    assert len(data.data) == N
    assert data.total > N


def test_parse_all(client: BrowseMusic) -> None:
    results = parsed_json(client, "all", category="Multipage")
    assert len(results) > 1
    # Every page is full except the last one, which holds the remainder.
    assert sum(len(result.data) for result in results) == results[0].total


def test_extract_data(client: BrowseMusic) -> None:
    loaded = loaded_json(client, 0)
    extracted_loaded = client.extract_data(loaded)

    data = parsed_json(client, 0)
    extracted_data = client.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == N


def test_extract_data_all(client: BrowseMusic) -> None:
    loaded = loaded_json(client, "all", category="Multipage")
    extracted_loaded = client.extract_data(loaded)

    data = parsed_json(client, "all", category="Multipage")
    extracted_data = client.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == data[0].total

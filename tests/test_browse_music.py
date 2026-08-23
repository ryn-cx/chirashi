# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.browse_music import N
from chirashi.browse_music.models import BrowseMusicModel
from chirashi.exceptions import StartOutOfRangeError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi


# TODO: Validate
class BrowseMusicTest(RecordedEndpoint):
    MODEL = BrowseMusicModel


# TODO: Validate
def test_download(client: Chirashi) -> None:
    BrowseMusicTest.download_test(0, lambda: client.browse_music.download(start=0))


# TODO: Validate
def test_download_all(client: Chirashi) -> None:
    BrowseMusicTest.download_test("all", client.browse_music.download_all, "Multipage")


# The catalogue is a few hundred artists, so a start this far out is always past
# the end of it.
# TODO: Validate
@pytest.mark.parametrize("start", [pytest.param(9999, id="start past the catalogue")])
def test_download_invalid(client: Chirashi, start: int) -> None:
    BrowseMusicTest.error_test(
        start,
        lambda: client.browse_music.download(start=start),
        StartOutOfRangeError,
    )


# TODO: Validate
def test_parse() -> None:
    BrowseMusicTest.parse_test(0)


# TODO: Validate
def test_parse_all() -> None:
    BrowseMusicTest.parse_test("all", "Multipage")


# TODO: Validate
def test_extract_data(client: Chirashi) -> None:
    loaded = BrowseMusicTest.recorded_documents(0)
    extracted_loaded = client.browse_music.extract_data(loaded)

    data = client.browse_music.load(BrowseMusicTest.recorded_content(0))
    extracted_data = client.browse_music.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == N


# TODO: Validate
def test_extract_data_all(client: Chirashi) -> None:
    loaded = BrowseMusicTest.recorded_documents("all", category="Multipage")
    extracted_loaded = client.browse_music.extract_data(loaded)

    data = [
        client.browse_music.load(page)
        for page in BrowseMusicTest.recorded_documents("all", "Multipage")
    ]
    extracted_data = client.browse_music.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == data[0].total

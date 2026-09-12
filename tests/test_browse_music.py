# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.browse_music import N
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from chirashi import Chirashi


# TODO: Validate
def test_download(client: Chirashi) -> None:
    catalogue = client.browse_music()
    assert len(catalogue.data) == N
    assert catalogue.total > N


# TODO: Validate
def test_download_all(client: Chirashi) -> None:
    pages = client.browse_music.load_pages(client.browse_music.download_all())
    assert len(client.browse_music.extract_data(pages)) == pages[0].total


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    # The catalogue is a few hundred artists, so a start this far out is always
    # past the end of it.
    with pytest.raises(StartOutOfRangeError):
        client.browse_music.download(start=9999)

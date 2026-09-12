# TODO: Validate
from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from chirashi.browse_series import N
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from chirashi import Chirashi


# TODO: Validate
def test_download(client: Chirashi) -> None:
    catalogue = client.browse_series()
    assert len(catalogue.data) == N
    assert catalogue.total > N


# TODO: Validate
def test_download_until_datetime(client: Chirashi) -> None:
    end_datetime = datetime.now().astimezone() - timedelta(days=7)
    pages = client.browse_series.load_pages(
        client.browse_series.download_until_datetime(end_datetime),
    )
    assert len(client.browse_series.extract_data(pages)) == len(pages) * N


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(StartOutOfRangeError):
        client.browse_series.download(start=9999)

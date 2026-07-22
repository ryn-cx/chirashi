# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.seasons import Seasons

SERIES_ID = "GEXH3W29Z"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Seasons:
    return client.seasons


class TestSeasons:
    def test_download(self, endpoint: Seasons) -> None:
        download_and_save(
            endpoint,
            SERIES_ID,
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: Seasons) -> None:
        # TODO: assert every season series id matches SERIES_ID (needs live data)
        data = parse_json(endpoint, SERIES_ID)
        assert data.data is not None

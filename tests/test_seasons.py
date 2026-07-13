# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.seasons import Seasons
    from chirashi.seasons.models import SeasonsModel

SERIES_ID = "GEXH3W29Z"
INVALID_SERIES_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Seasons:
    return client.seasons


@pytest.fixture(scope="session")
def json_file(endpoint: Seasons) -> Path:
    return data_path(endpoint, SERIES_ID)


@pytest.fixture(scope="session")
def data(endpoint: Seasons, json_file: Path) -> SeasonsModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSeasons:
    def test_download(self, endpoint: Seasons) -> None:
        download_if_missing(
            endpoint,
            SERIES_ID,
            lambda: endpoint.download(SERIES_ID),
        )

    def test_value(self, data: SeasonsModel) -> None:
        # TODO: assert every season series id matches SERIES_ID (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: Seasons) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SERIES_ID,
            lambda: endpoint.get(INVALID_SERIES_ID),
        )

# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.season_episodes import SeasonEpisodes
    from chirashi.season_episodes.models import SeasonEpisodesModel

SEASON_ID = "G68VCP0VQ"
INVALID_SEASON_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SeasonEpisodes:
    return client.season_episodes


@pytest.fixture(scope="session")
def json_file(endpoint: SeasonEpisodes) -> Path:
    return data_path(endpoint, SEASON_ID)


@pytest.fixture(scope="session")
def data(endpoint: SeasonEpisodes, json_file: Path) -> SeasonEpisodesModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSeasonEpisodes:
    def test_download(self, endpoint: SeasonEpisodes) -> None:
        download_if_missing(
            endpoint,
            SEASON_ID,
            lambda: endpoint.download(SEASON_ID),
        )

    def test_value(self, data: SeasonEpisodesModel) -> None:
        # TODO: assert every episode season id matches SEASON_ID and the count
        # is 12 (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: SeasonEpisodes) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEASON_ID,
            lambda: endpoint.get(INVALID_SEASON_ID),
        )

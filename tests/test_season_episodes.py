# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.season_episodes import SeasonEpisodes

SEASON_ID = "G68VCP0VQ"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SeasonEpisodes:
    return client.season_episodes


class TestSeasonEpisodes:
    def test_download(self, endpoint: SeasonEpisodes) -> None:
        download_and_save(
            endpoint,
            SEASON_ID,
            lambda: endpoint.download(SEASON_ID),
        )

    def test_parse(self, endpoint: SeasonEpisodes) -> None:
        # TODO: assert every episode season id matches SEASON_ID and the count
        # is 12 (needs live data)
        data = parse_json(endpoint, SEASON_ID)
        assert data.data is not None

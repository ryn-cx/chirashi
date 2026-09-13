# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from chirashi import Chirashi

SEASON_IDS = [pytest.param("G68VCP0VQ", id="#compass2.0 animation project season 1")]
SEASON_IDS_WITHOUT_EPISODES = [
    pytest.param("GGGGGGGGG", id="Season that does not exist"),
    pytest.param("GYJQC15DP", id="Season without episodes"),
]


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_download(client: Chirashi, season_id: str) -> None:
    episodes = client.season_episodes(season_id)
    assert episodes.total == len(episodes.data)
    assert all(episode.season_id == season_id for episode in episodes.data)


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS_WITHOUT_EPISODES)
def test_download_without_episodes(client: Chirashi, season_id: str) -> None:
    episodes = client.season_episodes(season_id)
    assert episodes.total == 0
    assert episodes.data == []

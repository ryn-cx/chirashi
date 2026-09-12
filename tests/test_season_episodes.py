# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeasonNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

SEASON_IDS = [pytest.param("G68VCP0VQ", id="#compass2.0 animation project season 1")]


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_download(client: Chirashi, season_id: str) -> None:
    episodes = client.season_episodes(season_id)
    assert episodes.total == len(episodes.data)
    assert all(episode.season_id == season_id for episode in episodes.data)


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(SeasonNotFoundError):
        client.season_episodes.download("GGGGGGGGG")

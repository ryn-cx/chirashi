from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeasonEpisodesNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.season_episodes import SeasonEpisodes

SEASON_ID = "G68VCP0VQ"
INVALID_SEASON_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> SeasonEpisodes:
    return client.season_episodes


def test_download(client: SeasonEpisodes) -> None:
    download_and_save(client, SEASON_ID, lambda: client.download(SEASON_ID))


def test_parse(client: SeasonEpisodes) -> None:
    data = parsed_json(client, SEASON_ID)
    assert data.data
    assert all(episode.season_id == SEASON_ID for episode in data.data)


def test_download_invalid(client: SeasonEpisodes) -> None:
    assert_error(
        client,
        INVALID_SEASON_ID,
        lambda: client.download(INVALID_SEASON_ID),
        SeasonEpisodesNotFoundError,
    )

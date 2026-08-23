# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import SeasonNotFoundError
from chirashi.season_episodes.models import SeasonEpisodesModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

SEASON_IDS = [pytest.param("G68VCP0VQ", id="#compass2.0 animation project season 1")]


# TODO: Validate
class SeasonEpisodesTest(RecordedEndpoint):
    MODEL = SeasonEpisodesModel


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_download(client: Chirashi, season_id: str) -> None:
    SeasonEpisodesTest.download_test(
        season_id,
        lambda: client.season_episodes.download(season_id),
    )


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_parse(season_id: str) -> None:
    SeasonEpisodesTest.parse_test(season_id)


# TODO: Validate
@pytest.mark.parametrize(
    "season_id",
    [pytest.param("GGGGGGGGG", id="season that does not exist")],
)
def test_download_invalid(client: Chirashi, season_id: str) -> None:
    SeasonEpisodesTest.error_test(
        season_id,
        lambda: client.season_episodes.download(season_id),
        SeasonNotFoundError,
    )

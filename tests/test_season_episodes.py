from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.season_episodes import SeasonEpisodes


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SeasonEpisodes:
    return client.season_episodes


class TestEpisodes:
    def test_get(self, endpoint: SeasonEpisodes) -> None:
        season_id = "G68VCP0VQ"
        episode_count = 12
        model = endpoint.get(season_id)
        assert all(episode.season_id == season_id for episode in model.data)
        assert len(model.data) == episode_count
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: SeasonEpisodes) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get("GGGGGGGGG")
        assert "data" in error.value.response

    def test_parse(self, endpoint: SeasonEpisodes) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.seasons import Seasons


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Seasons:
    return client.seasons


class TestSeasons:
    def test_get(self, endpoint: Seasons) -> None:
        season_id = "GEXH3W29Z"
        model = endpoint.get(season_id)
        assert all(season.series_id == season_id for season in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: Seasons) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get("GGGGGGGGG")
        assert "data" in error.value.response

    def test_parse(self, endpoint: Seasons) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

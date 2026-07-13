from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError
from tests.constants import INVALID_SEARCH_QUERY

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.episode import SearchEpisode


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchEpisode:
    return client.search.episode


class TestSearchEpisode:
    def test_get(self, endpoint: SearchEpisode) -> None:
        model = endpoint.get("This Is #COMPASS2.0")
        assert any(item.id == "GVWU8XW1Z" for item in model.data[0].items)
        assert model.data[0].type == "episode"
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: SearchEpisode) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: SearchEpisode) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

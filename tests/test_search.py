# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search import Search

INVALID_SEARCH_QUERY = "qwertyuiopasdfghjklzxcvbnm"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Search:
    return client.search


class TestSearch:
    def test_get(self, endpoint: Search) -> None:
        model = endpoint.get("#COMPASS2.0 ANIMATION PROJECT")
        assert any(
            series.id == "GEXH3W29Z" for series in endpoint.extract_series(model)
        )
        assert endpoint.extract_music(model)
        assert endpoint.extract_episode(model)
        assert endpoint.extract_top_results(model)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: Search) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_top_results(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            assert isinstance(endpoint.extract_top_results(model), list)

    def test_extract_series(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            assert isinstance(endpoint.extract_series(model), list)

    def test_extract_episode(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            assert isinstance(endpoint.extract_episode(model), list)

    def test_extract_music(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            assert isinstance(endpoint.extract_music(model), list)

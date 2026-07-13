from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError
from tests.constants import INVALID_SEARCH_QUERY

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.movie_listing import SearchMovieListing


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMovieListing:
    return client.search.movie_listing


class TestSearchMovieListing:
    def test_get(self, endpoint: SearchMovieListing) -> None:
        model = endpoint.get("009-1: The End of the Beginning")
        assert any(item.id == "GY8VX2G9YG" for item in model.data[0].items)
        assert model.data[0].type == "movie_listing"
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: SearchMovieListing) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: SearchMovieListing) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

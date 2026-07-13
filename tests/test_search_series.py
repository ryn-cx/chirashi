from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError
from tests.constants import INVALID_SEARCH_QUERY

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.series import SearchSeries


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchSeries:
    return client.search.series


class TestSearchSeries:
    def test_get(self, endpoint: SearchSeries) -> None:
        model = endpoint.get("#COMPASS2.0 ANIMATION PROJECT")
        endpoint.save_new_json_file(endpoint.original_input(model))
        assert any(item.id == "GEXH3W29Z" for item in model.data[0].items)

    def test_invalid_get(self, endpoint: SearchSeries) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: SearchSeries) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

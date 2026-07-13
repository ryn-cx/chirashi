from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError
from tests.constants import INVALID_SEARCH_QUERY

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.music import SearchMusic


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMusic:
    return client.search.music


class TestSearchMusic:
    def test_get(self, endpoint: SearchMusic) -> None:
        model = endpoint.get("CASANOVA POSSE ")
        assert any(item.id == "MV5ADCC418" for item in model.data[0].items)
        assert all(datum.type == "music" for datum in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: SearchMusic) -> None:
        with pytest.raises(NoContentError) as error:
            endpoint.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response

    def test_parse(self, endpoint: SearchMusic) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

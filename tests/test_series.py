from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import HTTPError

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.series import Series


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Series:
    return client.series


class TestSeries:
    def test_get(self, endpoint: Series) -> None:
        series_id = "GG5H5XQX4"
        model = endpoint.get(series_id)
        assert any(datum.id == series_id for datum in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self, endpoint: Series) -> None:
        with pytest.raises(HTTPError):
            endpoint.get("GGGGGGGGG")

    def test_parse(self, endpoint: Series) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

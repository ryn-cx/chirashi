from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.objects import Objects

OBJECT_IDS = ["GE00258180JAJP"]
INVALID_OBJECT_ID = "GGGGGGGGGGGGG"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Objects:
    return client.objects


class TestObjects:
    @pytest.mark.parametrize("object_id", OBJECT_IDS)
    def test_download(self, endpoint: Objects, object_id: str) -> None:
        download_if_missing(
            endpoint,
            object_id,
            lambda: endpoint.download(object_id),
        )

    @pytest.mark.parametrize("object_id", OBJECT_IDS)
    def test_value(self, endpoint: Objects, object_id: str) -> None:
        raw = data_path(endpoint, object_id).read_text()
        data = endpoint.parse(json.loads(raw))
        assert data.data[0].id == object_id

    def test_invalid(self, endpoint: Objects) -> None:
        assert_http_error(
            endpoint,
            INVALID_OBJECT_ID,
            lambda: endpoint.download(INVALID_OBJECT_ID),
        )

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

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
        download_and_save(
            endpoint,
            object_id,
            lambda: endpoint.download(object_id),
        )

    @pytest.mark.parametrize("object_id", OBJECT_IDS)
    def test_parse(self, endpoint: Objects, object_id: str) -> None:
        data = parse_json(endpoint, object_id)
        assert data.data[0].id == object_id

    def test_invalid_download(self, endpoint: Objects) -> None:
        assert_error(
            endpoint,
            INVALID_OBJECT_ID,
            lambda: endpoint.download(INVALID_OBJECT_ID),
            HTTPError,
        )

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.search.music import SearchMusic

QUERY = "CASANOVA POSSE "


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMusic:
    return client.search.music


class TestSearchMusic:
    def test_download(self, endpoint: SearchMusic) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchMusic) -> None:
        # TODO: assert the expected music id is present and every datum type is
        # music (needs live data)
        data = parse_json(endpoint, QUERY)
        assert data.data is not None

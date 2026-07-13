# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.constants import INVALID_SEARCH_QUERY
from tests.utils import assert_no_content_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi
    from chirashi.search.music import SearchMusic
    from chirashi.search.music.models import SearchMusicModel

QUERY = "CASANOVA POSSE "


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchMusic:
    return client.search.music


@pytest.fixture(scope="session")
def json_file(endpoint: SearchMusic) -> Path:
    return data_path(endpoint, QUERY)


@pytest.fixture(scope="session")
def data(endpoint: SearchMusic, json_file: Path) -> SearchMusicModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSearchMusic:
    def test_download(self, endpoint: SearchMusic) -> None:
        download_if_missing(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_value(self, data: SearchMusicModel) -> None:
        # TODO: assert the expected music id is present and every datum type is
        # music (needs live data)
        assert data.data is not None

    def test_invalid(self, endpoint: SearchMusic) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.get(INVALID_SEARCH_QUERY),
        )

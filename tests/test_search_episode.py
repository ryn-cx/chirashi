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
    from chirashi.search.episode import SearchEpisode
    from chirashi.search.episode.models import SearchEpisodeModel

QUERY = "This Is #COMPASS2.0"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> SearchEpisode:
    return client.search.episode


@pytest.fixture(scope="session")
def json_file(endpoint: SearchEpisode) -> Path:
    return data_path(endpoint, QUERY)


@pytest.fixture(scope="session")
def data(endpoint: SearchEpisode, json_file: Path) -> SearchEpisodeModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSearchEpisode:
    def test_download(self, endpoint: SearchEpisode) -> None:
        download_if_missing(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_value(self, data: SearchEpisodeModel) -> None:
        # TODO: assert the expected episode id and type are present (needs live
        # data)
        assert data.data is not None

    def test_invalid(self, endpoint: SearchEpisode) -> None:
        assert_no_content_error(
            endpoint,
            INVALID_SEARCH_QUERY,
            lambda: endpoint.get(INVALID_SEARCH_QUERY),
        )

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.browse_series import Browse

START = 0


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Browse:
    return client.browse_series


class TestBrowseSeries:
    def test_download(self, endpoint: Browse) -> None:
        download_and_save(
            endpoint,
            str(START),
            lambda: endpoint.download(start=START),
        )

    def test_parse(self, endpoint: Browse) -> None:
        # TODO: assert the total and per-page entry counts (needs live data)
        data = parse_json(endpoint, str(START))
        assert data.data is not None

    def test_compile_entries_from_single_browse(self, endpoint: Browse) -> None:
        data = parse_json(endpoint, str(START))
        entries = endpoint.compile_entries(data)
        assert entries == data.data

    def test_compile_entries_from_list_of_browses(self, endpoint: Browse) -> None:
        models = [parse_json(endpoint, str(START))]
        entries = endpoint.compile_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected


@pytest.mark.parametrize("start", [None, 36])
def test_log_id(endpoint: Browse, start: int | None) -> None:
    expected = f"Browse start={start!r}"
    assert endpoint.get_log_id(start=start) == expected

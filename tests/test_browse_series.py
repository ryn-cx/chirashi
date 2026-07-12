from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.browse_series import Browse

DEFAULT_ENTRIES_PER_PAGE = 36


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Browse:
    return client.browse_series


class TestBrowseSeries:
    def test_get(self, endpoint: Browse) -> None:
        model = endpoint.get()
        assert model.total > DEFAULT_ENTRIES_PER_PAGE
        assert len(model.data) == DEFAULT_ENTRIES_PER_PAGE
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_since_datetime(self, endpoint: Browse) -> None:
        first_page = endpoint.get()
        end_datetime = first_page.data[-1].last_public
        responses = endpoint.get_since_datetime(end_datetime)
        first_page_count = len(endpoint.compile_entries(first_page))
        paginated_count = len(endpoint.compile_entries(responses))
        assert paginated_count == first_page_count * 2

    def test_get_last_page(self, endpoint: Browse) -> None:
        first_page = endpoint.get()
        model = endpoint.get(start=first_page.total - DEFAULT_ENTRIES_PER_PAGE)
        assert len(model.data) == DEFAULT_ENTRIES_PER_PAGE
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_past_last_page(self, endpoint: Browse) -> None:
        first_page = endpoint.get()
        with pytest.raises(NoContentError):
            endpoint.get(start=first_page.total)

    def test_parse(self, endpoint: Browse) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_entries_from_single_browse(self, endpoint: Browse) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            entries = endpoint.compile_entries(model)
            assert entries == model.data

    def test_extract_entries_from_list_of_browses(self, endpoint: Browse) -> None:
        json_files = endpoint.json_files()
        models = [endpoint.parse(json.loads(f.read_text())) for f in json_files]
        entries = endpoint.compile_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected

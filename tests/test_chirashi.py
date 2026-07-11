# TODO: Validate
from __future__ import annotations

import json

import pytest
from get_around import build_client_automatically

from chirashi import Chirashi
from chirashi.exceptions import HTTPError, NoContentError

client = Chirashi(build_client_automatically())

SEARCH_QUERY = "Frieren"
SERIES_ID = "GG5H5XQX4"
"""series_id of Frieren."""
SEASON_ID = "GYE5CQMQ5"
"""season_id of a Frieren season 1."""
INVALID_ID = "GGGGGGGGG"
INVALID_SEARCH_QUERY = "qwertyuiopasdfghjklzxcvbnm"
DEFAULT_ENTRIES_PER_PAGE = 36


class TestGet:
    def test_get_browse_series(self) -> None:
        endpoint = client.browse_series
        model = endpoint.get()
        assert model.total > DEFAULT_ENTRIES_PER_PAGE
        assert len(model.data) == DEFAULT_ENTRIES_PER_PAGE
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_browse_series_since_datetime(self) -> None:
        endpoint = client.browse_series
        first_page = endpoint.get()
        end_datetime = first_page.data[-1].last_public
        responses = endpoint.get_since_datetime(end_datetime)
        first_page_count = len(endpoint.compile_entries(first_page))
        paginated_count = len(endpoint.compile_entries(responses))
        assert paginated_count > first_page_count

    def test_get_browse_series_past_last_page(self) -> None:
        endpoint = client.browse_series
        first_page = endpoint.get()
        model = endpoint.get(start=first_page.total - DEFAULT_ENTRIES_PER_PAGE)
        assert len(model.data) == DEFAULT_ENTRIES_PER_PAGE
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_series(self) -> None:
        endpoint = client.series
        model = endpoint.get(SERIES_ID)
        assert any(datum.id == SERIES_ID for datum in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_seasons(self) -> None:
        endpoint = client.seasons
        model = endpoint.get(SERIES_ID)
        assert all(season.series_id == SERIES_ID for season in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_episodes(self) -> None:
        endpoint = client.episodes
        model = endpoint.get(SEASON_ID)
        assert all(episode.season_id == SEASON_ID for episode in model.data)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_search(self) -> None:
        endpoint = client.search
        model = endpoint.get(SEARCH_QUERY)
        assert any(series.id == SERIES_ID for series in model.series)
        assert model.music
        assert model.episode
        assert model.top_results
        endpoint.save_new_json_file(endpoint.original_input(model))


class TestInvalidGet:
    def test_invalid_get_browse_series(self) -> None:
        pytest.skip("This cannot be tested.")

    def test_invalid_get_series(self) -> None:
        with pytest.raises(HTTPError):
            client.series.get(INVALID_ID)

    def test_invalid_get_seasons(self) -> None:
        # This endpoint does not return an HTTP error when no match is found, it
        # instead returns an empty list, which surfaces as NoContentError.
        with pytest.raises(NoContentError) as error:
            client.seasons.get(INVALID_ID)
        # The payload is still recoverable from the raised exception.
        assert "data" in error.value.response

    def test_invalid_get_episodes(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.episodes.get(INVALID_ID)
        assert "data" in error.value.response

    def test_invalid_get_search(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.search.get(INVALID_SEARCH_QUERY)
        assert "data" in error.value.response


class TestParse:
    @pytest.mark.parametrize(
        "endpoint_name",
        ["browse_series", "series", "seasons", "episodes", "search"],
    )
    def test_parse(self, endpoint_name: str) -> None:
        endpoint = getattr(client, endpoint_name)
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))


class TestExtract:
    def test_extract_browse_series_entries(self) -> None:
        for json_file in client.browse_series.json_files():
            model = client.browse_series.parse(json.loads(json_file.read_text()))
            entries = client.browse_series.compile_entries(model)
            assert entries == model.data

    def test_extract_browse_series_entries_from_list(self) -> None:
        json_files = client.browse_series.json_files()
        models = [
            client.browse_series.parse(json.loads(f.read_text())) for f in json_files
        ]
        entries = client.browse_series.compile_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected

    @pytest.mark.parametrize(
        "attribute",
        ["music", "series", "episode", "top_results"],
    )
    def test_extract_search(self, attribute: str) -> None:
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            assert isinstance(getattr(model, attribute), list)

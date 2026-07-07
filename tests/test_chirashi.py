# TODO: Validate
"""Test for chirashi."""

from __future__ import annotations

import json
import os
from datetime import datetime

import pytest
from dotenv import load_dotenv

from chirashi import Chirashi
from chirashi.exceptions import HTTPError, LoginError
from chirashi.search.episodes import SearchEpisode
from chirashi.search.music import SearchMusic
from chirashi.search.series import SearchSeries
from chirashi.search.top_results import SearchTopResults

load_dotenv()

client = Chirashi(
    get_around_server=os.environ["GET_AROUND_SERVER"],
    get_around_password=os.environ["GET_AROUND_PASSWORD"],
)
logged_in_client = Chirashi(
    username=os.environ["CRUNCHYROLL_USERNAME"],
    password=os.environ["CRUNCHYROLL_PASSWORD"],
)

DEFAULT_ENTRIES_PER_PAGE = 36

# Run the main get tests against both an anonymous and a logged-in client.
CLIENTS = pytest.mark.parametrize(
    "api",
    [client, logged_in_client],
    ids=["anon", "logged_in"],
)


class TestBrowseSeries:
    """Test the browse series endpoint."""

    @CLIENTS
    def test_get(self, api: Chirashi) -> None:
        """Test getting browse series."""
        model = api.browse_series.get()
        api.browse_series.save_new_json_file(api.browse_series.dump(model))
        expected_count = DEFAULT_ENTRIES_PER_PAGE
        assert expected_count < model.total
        assert len(model.data) == expected_count

    def test_invalid_get(self) -> None:
        """Test getting an invalid browse series."""
        pytest.skip("This cannot be tested.")

    def test_get_since_datetime(self) -> None:
        """Test getting browse series since a datetime."""
        first_page = client.browse_series.get()
        end_datetime = first_page.data[-1].last_public
        response = client.browse_series.get_since_datetime(end_datetime)
        first_page_count = len(client.browse_series.extract_entries(first_page))
        paginated_count = len(client.browse_series.extract_entries(response))

        assert paginated_count > first_page_count

    def test_get_past_last_page(self) -> None:
        """Test getting the last browse series page."""
        first_page = client.browse_series.get()
        past_end = client.browse_series.get(
            start=first_page.total - DEFAULT_ENTRIES_PER_PAGE,
        )
        client.browse_series.save_new_json_file(client.browse_series.dump(past_end))
        assert len(past_end.data) == DEFAULT_ENTRIES_PER_PAGE

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.browse_series.json_files():
            client.browse_series.parse(json.loads(json_file.read_text()))

    def test_extract_entries(self) -> None:
        """Test extracting browse series entries."""
        for json_file in client.browse_series.json_files():
            model = client.browse_series.parse(json.loads(json_file.read_text()))
            entries = client.browse_series.extract_entries(model)
            assert entries == model.data

    def test_extract_entries_from_list(self) -> None:
        """Test extracting browse series entries from a list."""
        json_files = client.browse_series.json_files()
        models = [
            client.browse_series.parse(json.loads(f.read_text())) for f in json_files
        ]

        entries = client.browse_series.extract_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected


class TestSeries:
    """Test the series endpoint."""

    @CLIENTS
    def test_get(self, api: Chirashi) -> None:
        """Test getting series."""
        model = api.series.get("GG5H5XQX4")
        api.series.save_new_json_file(api.series.dump(model))
        expected_count = 1
        assert len(model.data) == expected_count == model.total
        assert model.data[0].id == "GG5H5XQX4"

    def test_invalid_get(self) -> None:
        """Test getting an invalid series."""
        with pytest.raises(HTTPError):
            client.series.get("GGGGGGGGG")

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.series.json_files():
            client.series.parse(json.loads(json_file.read_text()))


class TestSeasons:
    """Test the seasons endpoint."""

    @CLIENTS
    def test_get(self, api: Chirashi) -> None:
        """Test getting seasons."""
        model = api.seasons.get("GG5H5XQX4")
        api.seasons.save_new_json_file(api.seasons.dump(model))
        expected_count = 2
        assert len(model.data) == expected_count == model.total
        for data in model.data:
            assert data.series_id == "GG5H5XQX4"

    def test_invalid_get(self) -> None:
        """Test getting invalid seasons."""
        # This endpoint does not return an HTTP error when no match is found, it
        # instead returns an empty list.
        model = client.seasons.get("GGGGGGGGG")
        client.seasons.save_new_json_file(client.seasons.dump(model))
        assert model.data == []
        assert model.total == 0

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.seasons.json_files():
            client.seasons.parse(json.loads(json_file.read_text()))


class TestEpisodes:
    """Test the episodes endpoint."""

    @CLIENTS
    def test_get(self, api: Chirashi) -> None:
        """Test getting episodes."""
        model = api.episodes.get("GYE5CQMQ5")
        api.episodes.save_new_json_file(api.episodes.dump(model))
        expected_count = 28
        assert len(model.data) == expected_count == model.total
        for data in model.data:
            assert data.season_id == "GYE5CQMQ5"

    def test_invalid_get(self) -> None:
        """Test getting invalid episodes."""
        model = client.episodes.get("GGGGGGGGG")
        client.episodes.save_new_json_file(client.episodes.dump(model))
        assert model.data == []
        assert model.total == 0

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.episodes.json_files():
            client.episodes.parse(json.loads(json_file.read_text()))


class TestSearch:
    """Test the search endpoint."""

    def test_get_series(self) -> None:
        """Test getting search results."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        expected_count = 4  # Search results are grouped into 4 categories.
        assert len(model.data) == expected_count == model.total
        assert client.search.extract_series(model)[0].id == "GG5H5XQX4"

    def test_get_music(self) -> None:
        """Test extracting music items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        client.search.extract_music(model)
        assert any(datum.type == "music" for datum in model.data)

    def test_get_episodes(self) -> None:
        """Test extracting episode items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        client.search.extract_episodes(model)
        assert any(datum.type == "episode" for datum in model.data)

    def test_get_top_results(self) -> None:
        """Test extracting top results items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        client.search.extract_top_results(model)
        assert any(datum.type == "top_results" for datum in model.data)

    def test_invalid_get(self) -> None:
        """Test searching for a query with no results."""
        model = client.search.get("qwertyuiopasdfghjklzxcvbnm")
        client.search.save_new_json_file(client.search.dump(model))
        expected_count = 0  # When no results are found no categories are returned
        assert len(model.data) == expected_count == model.total

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))

    def test_extract_music(self) -> None:
        """Test extracting music items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_music(model)

    def test_extract_series(self) -> None:
        """Test extracting series items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_series(model)

    def test_extract_episodes(self) -> None:
        """Test extracting episode items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_episodes(model)

    def test_extract_top_results(self) -> None:
        """Test extracting top results items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_top_results(model)


class TestSearchMusic:
    """Test the search music endpoint."""

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in SearchMusic.json_files():
            SearchMusic.parse(json.loads(json_file.read_text()))


class TestSearchSeries:
    """Test the search series endpoint."""

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in SearchSeries.json_files():
            SearchSeries.parse(json.loads(json_file.read_text()))


class TestSearchEpisode:
    """Test the search episode endpoint."""

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in SearchEpisode.json_files():
            SearchEpisode.parse(json.loads(json_file.read_text()))


class TestSearchTopResults:
    """Test the search top results endpoint."""

    def test_parse(self) -> None:
        """Test parsing every saved file."""
        for json_file in SearchTopResults.json_files():
            SearchTopResults.parse(json.loads(json_file.read_text()))


class TestLogin:
    """Test logging in with credentials."""

    def test_login_method(self) -> None:
        """Test logging in."""
        login_client = Chirashi()
        login_client.login(
            username=os.environ["CRUNCHYROLL_USERNAME"],
            password=os.environ["CRUNCHYROLL_PASSWORD"],
        )
        login_client.browse_series.get()

    def test_login_method_invalid(self) -> None:
        """Test logging in with invalid credentials directly."""
        login_client = Chirashi()
        with pytest.raises(LoginError):
            login_client.login(
                username="user@example.com",
                password="password",  # noqa: S106
            )

    def test_login_invalid(self) -> None:
        """Test logging in with invalid credentials indirectly."""
        invalid_client = Chirashi(
            username="user@example.com",
            password="password",  # noqa: S106
        )
        with pytest.raises(LoginError):
            invalid_client.browse_series.get()

    def test_logout(self) -> None:
        """Test logging out reverts to anonymous access."""
        login_client = Chirashi()
        login_client.login(
            username=os.environ["CRUNCHYROLL_USERNAME"],
            password=os.environ["CRUNCHYROLL_PASSWORD"],
        )
        login_client.browse_series.get()
        login_client.logout()
        assert login_client.anonymous

    def test_refresh_token(self) -> None:
        """Test that the token automatically refreshes when expired."""
        logged_in_client.browse_series.get()
        logged_in_client._token_expires_at = datetime.now().astimezone()  # noqa: SLF001 # type: ignore[reportPrivateUsage]
        logged_in_client.browse_series.get()

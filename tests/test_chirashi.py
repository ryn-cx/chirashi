# TODO: Validate
"""Test for chirashi."""

from __future__ import annotations

import json
from datetime import datetime
from typing import TYPE_CHECKING

import keyring
import pytest

from chirashi import Chirashi
from chirashi.exceptions import HTTPError, LoginError

if TYPE_CHECKING:
    from collections.abc import Iterator

KEYRING_SERVICE = "chirashi"
ETP_RT_KEY = "CRUNCHYROLL_ETP_RT"


def get_credential(name: str) -> str:
    """Return a secret from the Windows Credential Manager (via keyring)."""
    value = keyring.get_password(KEYRING_SERVICE, name)
    if value is None:
        msg = f"Missing credential {name!r}; run: keyring set {KEYRING_SERVICE} {name}"
        raise RuntimeError(msg)
    return value


GET_AROUND_SERVER = get_credential("GET_AROUND_SERVER")
GET_AROUND_PASSWORD = get_credential("GET_AROUND_PASSWORD")

client = Chirashi(
    get_around_server=GET_AROUND_SERVER,
    get_around_password=GET_AROUND_PASSWORD,
)
logged_in_client = Chirashi(
    username=get_credential("CRUNCHYROLL_USERNAME"),
    password=get_credential("CRUNCHYROLL_PASSWORD"),
    etp_rt=keyring.get_password(KEYRING_SERVICE, ETP_RT_KEY),
    get_around_server=GET_AROUND_SERVER,
    get_around_password=GET_AROUND_PASSWORD,
)


DEFAULT_ENTRIES_PER_PAGE = 36

# Toggle for the login/auth tests. They exercise Crunchyroll's rate-limited SSO
# login, so they are disabled by default; flip to True to run them.
RUN_LOGIN_TESTS = False

requires_login = pytest.mark.skipif(
    not RUN_LOGIN_TESTS,
    reason="Login tests are disabled (set RUN_LOGIN_TESTS = True to enable).",
)


class TestGet:
    """Test live get requests across every endpoint."""

    def test_get_browse_series(self) -> None:
        """Test getting browse series."""
        model = client.browse_series.get()
        client.browse_series.save_new_json_file(client.browse_series.dump(model))
        expected_count = DEFAULT_ENTRIES_PER_PAGE
        assert expected_count < model.total
        assert len(model.data) == expected_count

    def test_get_browse_series_since_datetime(self) -> None:
        """Test getting browse series since a datetime."""
        first_page = client.browse_series.get()
        end_datetime = first_page.data[-1].last_public
        response = client.browse_series.get_since_datetime(end_datetime)
        first_page_count = len(client.browse_series.extract_entries(first_page))
        paginated_count = len(client.browse_series.extract_entries(response))

        assert paginated_count > first_page_count

    def test_get_browse_series_past_last_page(self) -> None:
        """Test getting the last browse series page."""
        first_page = client.browse_series.get()
        past_end = client.browse_series.get(
            start=first_page.total - DEFAULT_ENTRIES_PER_PAGE,
        )
        client.browse_series.save_new_json_file(client.browse_series.dump(past_end))
        assert len(past_end.data) == DEFAULT_ENTRIES_PER_PAGE

    def test_get_series(self) -> None:
        """Test getting series."""
        model = client.series.get("GG5H5XQX4")
        client.series.save_new_json_file(client.series.dump(model))
        expected_count = 1
        assert len(model.data) == expected_count == model.total
        assert model.data[0].id == "GG5H5XQX4"

    def test_get_seasons(self) -> None:
        """Test getting seasons."""
        model = client.seasons.get("GG5H5XQX4")
        client.seasons.save_new_json_file(client.seasons.dump(model))
        expected_count = 2
        assert len(model.data) == expected_count == model.total
        for data in model.data:
            assert data.series_id == "GG5H5XQX4"

    def test_get_episodes(self) -> None:
        """Test getting episodes."""
        model = client.episodes.get("GYE5CQMQ5")
        client.episodes.save_new_json_file(client.episodes.dump(model))
        expected_count = 28
        assert len(model.data) == expected_count == model.total
        for data in model.data:
            assert data.season_id == "GYE5CQMQ5"

    def test_get_search_series(self) -> None:
        """Test getting series items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        assert model.series[0].id == "GG5H5XQX4"

    def test_get_search_music(self) -> None:
        """Test getting music items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        assert model.music

    def test_get_search_episodes(self) -> None:
        """Test getting episode items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        assert model.episode

    def test_get_search_top_results(self) -> None:
        """Test getting top results items from a live search."""
        model = client.search.get("Frieren")
        client.search.save_new_json_file(client.search.dump(model))
        assert model.top_results

    @requires_login
    def test_login_method(self) -> None:
        """Test logging in."""
        login_client = Chirashi(
            get_around_server=GET_AROUND_SERVER,
            get_around_password=GET_AROUND_PASSWORD,
        )
        login_client.login(
            username=get_credential("CRUNCHYROLL_USERNAME"),
            password=get_credential("CRUNCHYROLL_PASSWORD"),
        )
        login_client.browse_series.get()

    @requires_login
    def test_logout(self) -> None:
        """Test logging out reverts to anonymous access."""
        login_client = Chirashi(
            get_around_server=GET_AROUND_SERVER,
            get_around_password=GET_AROUND_PASSWORD,
        )
        login_client.login(
            username=get_credential("CRUNCHYROLL_USERNAME"),
            password=get_credential("CRUNCHYROLL_PASSWORD"),
        )
        login_client.browse_series.get()
        login_client.logout()
        assert login_client.anonymous

    @requires_login
    def test_refresh_token(self) -> None:
        """Test that the token automatically refreshes when expired."""
        logged_in_client.browse_series.get()
        logged_in_client._token_expires_at = datetime.now().astimezone()  # noqa: SLF001 # type: ignore[reportPrivateUsage]
        logged_in_client.browse_series.get()


class TestInvalidGet:
    """Test get requests for missing or invalid resources."""

    def test_invalid_get_browse_series(self) -> None:
        """Test getting an invalid browse series."""
        pytest.skip("This cannot be tested.")

    def test_invalid_get_series(self) -> None:
        """Test getting an invalid series."""
        with pytest.raises(HTTPError):
            client.series.get("GGGGGGGGG")

    def test_invalid_get_seasons(self) -> None:
        """Test getting invalid seasons."""
        # This endpoint does not return an HTTP error when no match is found, it
        # instead returns an empty list.
        model = client.seasons.get("GGGGGGGGG")
        client.seasons.save_new_json_file(client.seasons.dump(model))
        assert model.data == []
        assert model.total == 0

    def test_invalid_get_episodes(self) -> None:
        """Test getting invalid episodes."""
        model = client.episodes.get("GGGGGGGGG")
        client.episodes.save_new_json_file(client.episodes.dump(model))
        assert model.data == []
        assert model.total == 0

    def test_invalid_get_search(self) -> None:
        """Test searching for a query with no results."""
        model = client.search.get("qwertyuiopasdfghjklzxcvbnm")
        client.search.save_new_json_file(client.search.dump(model))
        assert model.music == model.series == model.episode == model.top_results == []

    @requires_login
    def test_login_method_invalid(self) -> None:
        """Test logging in with invalid credentials directly."""
        login_client = Chirashi(
            get_around_server=GET_AROUND_SERVER,
            get_around_password=GET_AROUND_PASSWORD,
        )
        with pytest.raises(LoginError):
            login_client.login(
                username="user@example.com",
                password="password",  # noqa: S106
            )

    @requires_login
    def test_login_invalid(self) -> None:
        """Test logging in with invalid credentials indirectly."""
        invalid_client = Chirashi(
            username="user@example.com",
            password="password",  # noqa: S106
            get_around_server=GET_AROUND_SERVER,
            get_around_password=GET_AROUND_PASSWORD,
        )
        with pytest.raises(LoginError):
            invalid_client.browse_series.get()


class TestParse:
    """Test parsing every saved file for each endpoint."""

    def test_parse_browse_series(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.browse_series.json_files():
            client.browse_series.parse(json.loads(json_file.read_text()))

    def test_parse_series(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.series.json_files():
            client.series.parse(json.loads(json_file.read_text()))

    def test_parse_seasons(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.seasons.json_files():
            client.seasons.parse(json.loads(json_file.read_text()))

    def test_parse_episodes(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.episodes.json_files():
            client.episodes.parse(json.loads(json_file.read_text()))

    def test_parse_search(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))


class TestExtract:
    """Test extracting typed entries from saved responses."""

    def test_extract_browse_series_entries(self) -> None:
        """Test extracting browse series entries."""
        for json_file in client.browse_series.json_files():
            model = client.browse_series.parse(json.loads(json_file.read_text()))
            entries = client.browse_series.extract_entries(model)
            assert entries == model.data

    def test_extract_browse_series_entries_from_list(self) -> None:
        """Test extracting browse series entries from a list."""
        json_files = client.browse_series.json_files()
        models = [
            client.browse_series.parse(json.loads(f.read_text())) for f in json_files
        ]

        entries = client.browse_series.extract_entries(models)
        expected = [datum for model in models for datum in model.data]
        assert entries == expected

    def test_extract_search_music(self) -> None:
        """Test extracting music items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            assert isinstance(model.music, list)

    def test_extract_search_series(self) -> None:
        """Test extracting series items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            assert isinstance(model.series, list)

    def test_extract_search_episodes(self) -> None:
        """Test extracting episode items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            assert isinstance(model.episode, list)

    def test_extract_search_top_results(self) -> None:
        """Test extracting top results items from search results."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            assert isinstance(model.top_results, list)

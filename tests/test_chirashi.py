"""Tests for chirashi."""

import json
import os
from datetime import datetime, timedelta

import pytest
from dotenv import load_dotenv

from chirashi import Chirashi
from chirashi.exceptions import HTTPError, LoginError

load_dotenv()

client = Chirashi(
    get_around_server=os.environ["GET_AROUND_SERVER"],
    get_around_password=os.environ["GET_AROUND_PASSWORD"],
)
logged_in_client = Chirashi(
    username=os.environ["CRUNCHYROLL_USERNAME"],
    password=os.environ["CRUNCHYROLL_PASSWORD"],
    get_around_server=os.environ["GET_AROUND_SERVER"],
    get_around_password=os.environ["GET_AROUND_PASSWORD"],
)


class TestParse:
    """Tests parsing files."""

    def test_parse_browse_series(self) -> None:
        """Test parsing browse series files."""
        for json_file in client.browse_series.json_files():
            client.browse_series.parse(json.loads(json_file.read_text()))

    def test_parse_series(self) -> None:
        """Test parsing series files."""
        for json_file in client.series.json_files():
            client.series.parse(json.loads(json_file.read_text()))

    def test_parse_seasons(self) -> None:
        """Test parsing seasons files."""
        for json_file in client.seasons.json_files():
            client.seasons.parse(json.loads(json_file.read_text()))

    def test_parse_episodes(self) -> None:
        """Test parsing episodes files."""
        for json_file in client.episodes.json_files():
            client.episodes.parse(json.loads(json_file.read_text()))

    def test_parse_search(self) -> None:
        """Test parsing search files."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))


class TestExtract:
    """Tests extracting data."""

    class TestBrowseSeries:
        """Tests extracting browse series data."""

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
                client.browse_series.parse(json.loads(f.read_text()))
                for f in json_files
            ]

            entries = client.browse_series.extract_entries(models)
            expected = [datum for model in models for datum in model.data]
            assert entries == expected


class TestGet:
    """Tests getting data."""

    class TestValid:
        """Tests getting data with valid inputs."""

        def test_get_browse_series(self) -> None:
            """Test getting browse series."""
            client.browse_series.get()

        def test_get_series(self) -> None:
            """Test getting series."""
            client.series.get("GG5H5XQ0D")

        def test_get_seasons(self) -> None:
            """Test getting seasons."""
            client.seasons.get("GG5H5XQ0D")

        def test_get_episodes(self) -> None:
            """Test getting episodes."""
            client.episodes.get("G619CPMQ1")

        def test_get_search(self) -> None:
            """Test getting search results."""
            client.search.get("shokjo")

        def test_get_browse_series_since_datetime(self) -> None:
            """Test getting browse series since a datetime."""
            first_page = client.browse_series.get()
            last_date_on_first_page = first_page.data[-1].last_public

            response = client.browse_series.get_since_datetime(
                end_datetime=last_date_on_first_page - timedelta(days=1),
            )

            assert len(client.browse_series.extract_entries(response)) >= 36  # noqa: PLR2004

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_series_invalid(self) -> None:
            """Test getting an invalid series."""
            with pytest.raises(HTTPError):
                client.series.get("zxcvbbnm")

        def test_get_seasons_invalid(self) -> None:
            """Test getting invalid seasons."""
            # This endpoint does not return an HTTP error when no match is found, it
            # instead returns an empty list.
            data = client.seasons.get("zxcvbbnm")
            assert data.data == []

        def test_get_episodes_invalid(self) -> None:
            """Test getting invalid episodes."""
            client.episodes.get("zxcvbbnm")

        def test_get_search_no_results(self) -> None:
            """Test searching for a query with no results."""
            client.search.get("zxcvbbnm")


class TestLogin:
    """Tests logging in with credentials."""

    def test_login(self) -> None:
        """Test logging in using environment variables."""
        logged_in_client.browse_series.get()

    def test_login_method(self) -> None:
        """Test logging in using the login method."""
        login_client = Chirashi(
            get_around_server=os.environ["GET_AROUND_SERVER"],
            get_around_password=os.environ["GET_AROUND_PASSWORD"],
        )
        login_client.login(
            username=os.environ["CRUNCHYROLL_USERNAME"],
            password=os.environ["CRUNCHYROLL_PASSWORD"],
        )
        login_client.browse_series.get()

    def test_login_method_invalid(self) -> None:
        """Test logging in using the login method with invalid credentials."""
        login_client = Chirashi(
            get_around_server=os.environ["GET_AROUND_SERVER"],
            get_around_password=os.environ["GET_AROUND_PASSWORD"],
        )
        with pytest.raises(LoginError):
            login_client.login(
                username="invalid@example.com",
                password="invalid",  # noqa: S106
            )

    def test_login_invalid(self) -> None:
        """Test logging in with invalid credentials."""
        invalid_client = Chirashi(
            username="invalid@example.com",
            password="invalid",  # noqa: S106
            get_around_server=os.environ["GET_AROUND_SERVER"],
            get_around_password=os.environ["GET_AROUND_PASSWORD"],
        )
        with pytest.raises(LoginError):
            invalid_client.browse_series.get()

    def test_logout(self) -> None:
        """Test logging out reverts to anonymous access."""
        login_client = Chirashi(
            get_around_server=os.environ["GET_AROUND_SERVER"],
            get_around_password=os.environ["GET_AROUND_PASSWORD"],
        )
        login_client.login(
            username=os.environ["CRUNCHYROLL_USERNAME"],
            password=os.environ["CRUNCHYROLL_PASSWORD"],
        )
        login_client.browse_series.get()
        login_client.logout()
        assert login_client.anonymous
        # Should still work as anonymous.
        login_client.browse_series.get()

    def test_refresh_token(self) -> None:
        """Test that the refresh token is used when the access token expires."""
        logged_in_client.browse_series.get()
        # Expire the token to force a refresh on the next request.
        logged_in_client._token_expires_at = datetime.now().astimezone()  # noqa: SLF001 # type: ignore[reportPrivateUsage]
        logged_in_client.browse_series.get()

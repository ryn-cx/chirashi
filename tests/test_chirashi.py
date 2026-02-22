"""Tests for chirashi."""

import json
from datetime import timedelta

import pytest

from chirashi import Chirashi
from chirashi.exceptions import HTTPError

client = Chirashi()


class TestParse:
    """Tests parsing files."""

    def test_parse_browse_series(self) -> None:
        """Test parsing browse series files."""
        for json_file in client.browse_series.json_files():
            file_content = json.loads(json_file.read_text())
            client.browse_series.parse(file_content)

    def test_parse_series(self) -> None:
        """Test parsing series files."""
        for json_file in client.series.json_files():
            file_content = json.loads(json_file.read_text())
            client.series.parse(file_content)

    def test_parse_seasons(self) -> None:
        """Test parsing seasons files."""
        for json_file in client.seasons.json_files():
            file_content = json.loads(json_file.read_text())
            client.seasons.parse(file_content)

    def test_parse_episodes(self) -> None:
        """Test parsing episodes files."""
        for json_file in client.episodes.json_files():
            file_content = json.loads(json_file.read_text())
            client.episodes.parse(file_content)


class TestExtract:
    """Tests extracting data."""

    class TestBrowseSeries:
        """Tests extracting browse series data."""

        def test_extract_browse_series_entries(self) -> None:
            """Test extracting browse series entries."""
            for json_file in client.browse_series.json_files():
                file_content = json.loads(json_file.read_text())
                model = client.browse_series.parse(file_content)
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
                client.series.get("GGGGGGGGG")

        def test_get_seasons_invalid(self) -> None:
            """Test getting invalid seasons."""
            # This endpoint does not return an HTTP error when no match is found, it
            # instead returns an empty list.
            data = client.seasons.get("GGGGGGGGG")
            assert data.data == []

        def test_get_episodes_invalid(self) -> None:
            """Test getting invalid episodes."""
            with pytest.raises(HTTPError):
                client.episodes.get("GGGGGGGGG")

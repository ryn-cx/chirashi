"""Exceptions."""

from __future__ import annotations

from typing import Any


class ChirashiError(Exception):
    """Base exception for Chirashi."""

    response: str | dict[str, Any] | None = None


class HTTPError(ChirashiError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


class EpisodeNotFoundError(ResourceNotFoundError):
    """Raised when the requested episode object does not exist."""

    def __init__(
        self,
        object_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the episode object id and the originating response."""
        self.object_id = object_id
        super().__init__(status_code, response)


class SeriesNotFoundError(ResourceNotFoundError):
    """Raised when the requested series does not exist."""

    def __init__(
        self,
        series_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id and the originating response."""
        self.series_id = series_id
        super().__init__(status_code, response)


class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season does not exist."""

    def __init__(
        self,
        season_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season id and the originating response."""
        self.season_id = season_id
        super().__init__(status_code, response)


class MusicVideoNotFoundError(ResourceNotFoundError):
    """Raised when the requested music video does not exist."""

    def __init__(
        self,
        music_video_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the music video id and the originating response."""
        self.music_video_id = music_video_id
        super().__init__(status_code, response)


class ConcertNotFoundError(ResourceNotFoundError):
    """Raised when the requested concert does not exist."""

    def __init__(
        self,
        concert_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the concert id and the originating response."""
        self.concert_id = concert_id
        super().__init__(status_code, response)


class ArtistNotFoundError(ResourceNotFoundError):
    """Raised when the requested artist does not exist."""

    def __init__(
        self,
        artist_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the artist id and the originating response."""
        self.artist_id = artist_id
        super().__init__(status_code, response)


class StartOutOfRangeError(ChirashiError, ValueError):
    """Raised when the requested start offset exceeds the total available items."""

    def __init__(self, start: int, total: int, response: dict[str, Any]) -> None:
        """Initialize with the start, available total, and original response."""
        self.start = start
        self.total = total
        self.response = response
        super().__init__(f"Requested start {start} exceeds total {total}")

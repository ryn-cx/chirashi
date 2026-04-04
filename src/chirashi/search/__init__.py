"""Search API endpoint."""

from __future__ import annotations

from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.search.models import Search as SearchModel


class Search(BaseEndpoint[SearchModel]):
    """Provides methods to download, parse, and retrieve search data."""

    _response_model = SearchModel

    def download(  # noqa: PLR0913
        self,
        query: str,
        *,
        n: int = 6,
        type: str = "music,series,episode,top_results,movie_listing",  # noqa: A002
        ratings: str = "true",
        preferred_audio_language: str = "ja-JP",
        locale: str = "en-US",
    ) -> dict[str, Any]:
        """Downloads search data for a given query.

        Args:
            query: The search query string.
            n: The number of results to return.
            type: Comma-separated content types to search.
            ratings: Whether to include ratings.
            preferred_audio_language: The preferred audio language.
            locale: The locale for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        params: dict[str, str | int] = {
            "q": query,
            "n": n,
            "type": type,
            "ratings": ratings,
            "preferred_audio_language": preferred_audio_language,
            "locale": locale,
        }

        headers = {"referer": "https://www.crunchyroll.com/search"}

        return self._client.download(
            "content/v2/discover/search",
            params,
            headers,
        )

    def get(  # noqa: PLR0913
        self,
        query: str,
        *,
        n: int = 6,
        type: str = "music,series,episode,top_results,movie_listing",  # noqa: A002
        ratings: str = "true",
        preferred_audio_language: str = "ja-JP",
        locale: str = "en-US",
    ) -> SearchModel:
        """Downloads and parses search data for a given query.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            query: The search query string.
            n: The number of results to return.
            type: Comma-separated content types to search.
            ratings: Whether to include ratings.
            preferred_audio_language: The preferred audio language.
            locale: The locale for the request.

        Returns:
            A Search model containing the parsed data.
        """
        data = self.download(
            query,
            n=n,
            type=type,
            ratings=ratings,
            preferred_audio_language=preferred_audio_language,
            locale=locale,
        )
        return self.parse(data)

# TODO: Validate
"""Search API endpoint."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, cast

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.search.models import Search as SearchModel

if TYPE_CHECKING:
    from good_ass_pydantic_integrator.constants import INPUT_TYPE


class Search(BaseEndpoint[SearchModel]):
    """Provides methods to download, parse, and retrieve search data."""

    _response_model = SearchModel

    def download(  # noqa: PLR0913
        self,
        query: str,
        *,
        n: int = 6,
        type: str = "music,series,episode,top_results",  # noqa: A002
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
        type: str = "music,series,episode,top_results",  # noqa: A002
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

    @classmethod
    def clean_data(cls, data: INPUT_TYPE) -> INPUT_TYPE:
        """Denormalize the grouped ``data`` list into one list per category.

        Crunchyroll returns search results as ``data: [{type, items, count},
        ...]``. This reshapes them into a top-level list per category so the
        single generated model exposes each type directly (``.music``,
        ``.series``, ``.episode``, ``.top_results``) instead of needing a
        separate class per category. Every category is always present, defaulting
        to an empty list so a no-result search still validates. The saved JSON
        corpus keeps the original grouped shape; this only runs on the way into
        parsing and model generation.

        Args:
            data: The raw JSON data, as downloaded/saved.

        Returns:
            The reshaped data with one list field per search category.
        """
        if not isinstance(data, Mapping) or "data" not in data:
            return data

        categories = ("top_results", "series", "episode", "music")
        grouped: dict[str, Any] = {category: [] for category in categories}
        for datum in cast("list[dict[str, Any]]", data["data"]):
            grouped[datum["type"]] = datum["items"]

        return {
            **grouped,
            "total": data["total"],
            "meta": data["meta"],
            "chirashi": data["chirashi"],
        }

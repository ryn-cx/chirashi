"""Contains the Search class."""

from __future__ import annotations

from typing import Any, override

from good_ass_pydantic_integrator import GAPIBaseModel

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.search.models import EpisodeItem, MusicItem, Series, TopResult
from chirashi.search.models import Search as SearchModel


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file."""

    _response_model = SearchModel

    def download(  # noqa: PLR0913
        self,
        query: str,
        *,
        n: int = 6,
        type: str = "music,series,episode,top_results",  # noqa: A002
        ratings: str = "true",
        preferred_audio_language: str = "ja-JP",
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the search file.

        Example request: https://www.crunchyroll.com/search?q=%23COMPASS2.0%20ANIMATION%20PROJECT
            GET /content/v2/discover/search?q=%23COMPASS2.0+ANIMATION+PROJECT&n=6&type=music,series,episode,top_results,movie_listing&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/search?q=%23COMPASS2.0%20ANIMATION%20PROJECT
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            TE: trailers
        """
        return self._client.download(
            "content/v2/discover/search",
            params={
                "q": query,
                "n": n,
                "type": type,
                "ratings": ratings,
                "preferred_audio_language": preferred_audio_language,
                "locale": locale or self._client.locale,
            },
            headers={"referer": "https://www.crunchyroll.com/search"},
            log_id=f"{self.__class__.__name__} {query}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return any(datum["items"] for datum in response.get("data", []))

    def get(  # noqa: PLR0913
        self,
        query: str,
        *,
        n: int = 6,
        type: str = "music,series,episode,top_results",  # noqa: A002
        ratings: str = "true",
        preferred_audio_language: str = "ja-JP",
        locale: str | None = None,
    ) -> SearchModel:
        """Downloads and parses the search file."""
        data = self.download(
            query,
            n=n,
            type=type,
            ratings=ratings,
            preferred_audio_language=preferred_audio_language,
            locale=locale,
        )
        return self._parse_or_raise(data, f"{self.__class__.__name__} {query}")

    def _extract_category[U: GAPIBaseModel](
        self,
        data: SearchModel,
        field_type: str,
        model: type[U],
    ) -> list[U]:
        for datum in data.data or []:
            if datum.type == field_type:
                return [
                    model.model_validate(item)
                    for item in self.original_input(datum.items)
                ]
        return []

    def extract_top_results(self, data: SearchModel) -> list[TopResult]:
        """Extract the top results from Search."""
        return self._extract_category(data, "top_results", TopResult)

    def extract_series(self, data: SearchModel) -> list[Series]:
        """Extract the series from Search."""
        return self._extract_category(data, "series", Series)

    def extract_episode(self, data: SearchModel) -> list[EpisodeItem]:
        """Extract the episodes from Search."""
        return self._extract_category(data, "episode", EpisodeItem)

    def extract_music(self, data: SearchModel) -> list[MusicItem]:
        """Extract the music from Search."""
        return self._extract_category(data, "music", MusicItem)

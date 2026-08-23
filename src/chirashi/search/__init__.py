"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import override

from chirashi.search.base import BaseSearch
from chirashi.search.models import Item, SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DEFAULT_TYPE = "music,series,episode,movie_listing,top_results"


class Search(BaseSearch[SearchModel]):
    """Manage the search file.

    Source: https://www.crunchyroll.com/search?q={query}

    Example request:
        - GET /content/v2/discover/search?
            - q={query}&
            - n=6&
            - type={type}&
            - ratings=true&
            - locale=en-US
            - HTTP/2
        - Host: www.crunchyroll.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Authorization: Bearer __REDACTED__
        - Connection: keep-alive
        - Referer: https://www.crunchyroll.com/search?q={query}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    MODEL = SearchModel
    LOAD = staticmethod(model_validate_json)
    search_type = DEFAULT_TYPE
    n = 6

    # TODO: Validate
    @override
    def __call__(
        self,
        q: str,
        *,
        n: int | None = None,
        search_type: str | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> SearchModel:
        """Run the search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                q,
                n=n,
                search_type=search_type,
                ratings=ratings,
                locale=locale,
            ),
            log_id,
        )

    # TODO: Validate
    @override
    def download(
        self,
        q: str,
        *,
        n: int | None = None,
        search_type: str | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> str:
        """Download the search file."""
        return self._download(
            q,
            n=n,
            search_type=search_type,
            ratings=ratings,
            locale=locale,
        )

    # TODO: Validate
    def _extract_category(self, data: SearchModel, field_type: str) -> list[Item]:
        """Return the items a search answered for one of the types it was asked."""
        for datum in data.data:
            if datum.type == field_type:
                return datum.items
        msg = f"No data found for field type '{field_type}' in search results."
        raise ValueError(msg)

    # TODO: Validate
    def extract_top_results(self, data: SearchModel) -> list[Item]:
        """Extract the top results from Search."""
        return self._extract_category(data, "top_results")

    # TODO: Validate
    def extract_series(self, data: SearchModel) -> list[Item]:
        """Extract the series from Search."""
        return self._extract_category(data, "series")

    # TODO: Validate
    def extract_episode(self, data: SearchModel) -> list[Item]:
        """Extract the episodes from Search."""
        return self._extract_category(data, "episode")

    # TODO: Validate
    def extract_music(self, data: SearchModel) -> list[Item]:
        """Extract the music from Search."""
        return self._extract_category(data, "music")

    # TODO: Validate
    def extract_movie_listing(self, data: SearchModel) -> list[Item]:
        """Extract the movie listings from Search."""
        return self._extract_category(data, "movie_listing")

"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import GAPIBaseModel

from chirashi.search.base import BaseSearch
from chirashi.search.episode.models import Item as EpisodeItem
from chirashi.search.models import Item, SearchModel
from chirashi.search.movie_listing.models import Item as MovieListingItem
from chirashi.search.music.models import Item as MusicItem
from chirashi.search.series.models import Item as SeriesItem

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

    _response_model = SearchModel
    search_type = DEFAULT_TYPE
    n = 6

    @override
    def download(
        self,
        q: str,
        *,
        n: int | None = None,
        search_type: str | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> dict[str, Any]:
        return self._download(
            q,
            n=n,
            search_type=search_type,
            ratings=ratings,
            locale=locale,
        )

    @override
    def download_and_parse(
        self,
        q: str,
        *,
        n: int | None = None,
        search_type: str | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> SearchModel:
        return self.parse(
            self.download(
                q,
                n=n,
                search_type=search_type,
                ratings=ratings,
                locale=locale,
            ),
        )

    def _extract_category[U: GAPIBaseModel](
        self,
        data: SearchModel,
        field_type: str,
        model: type[U],
    ) -> list[U]:
        for datum in data.data:
            if datum.type == field_type:
                return [
                    model.model_validate(item)
                    for item in self.original_input(datum.items)
                ]
        msg = f"No data found for field type '{field_type}' in search results."
        raise ValueError(msg)

    def extract_top_results(self, data: SearchModel) -> list[Item]:
        """Extract the top results from Search."""
        return self._extract_category(data, "top_results", Item)

    def extract_series(self, data: SearchModel) -> list[SeriesItem]:
        """Extract the series from Search."""
        return self._extract_category(data, "series", SeriesItem)

    def extract_episode(self, data: SearchModel) -> list[EpisodeItem]:
        """Extract the episodes from Search."""
        return self._extract_category(data, "episode", EpisodeItem)

    def extract_music(self, data: SearchModel) -> list[MusicItem]:
        """Extract the music from Search."""
        return self._extract_category(data, "music", MusicItem)

    def extract_movie_listing(self, data: SearchModel) -> list[MovieListingItem]:
        """Extract the movie listings from Search."""
        return self._extract_category(data, "movie_listing", MovieListingItem)

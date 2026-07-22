# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.search.episode import SearchEpisode
from chirashi.search.episode.models import Item as EpisodeItem
from chirashi.search.models import Item, SearchModel
from chirashi.search.movie_listing import SearchMovieListing
from chirashi.search.movie_listing.models import Item as MovieListingItem
from chirashi.search.music import SearchMusic
from chirashi.search.music.models import Item as MusicItem
from chirashi.search.series import SearchSeries
from chirashi.search.series.models import Item as SeriesItem

if TYPE_CHECKING:
    from chirashi import Chirashi

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DEFAULT_TYPE = "music,series,episode,top_results"


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file."""

    _response_model = SearchModel

    def __init__(self, client: Chirashi) -> None:
        """Initialize the search file."""
        super().__init__(client)
        self.movie_listing = SearchMovieListing(client)
        self.series = SearchSeries(client)
        self.music = SearchMusic(client)
        self.episode = SearchEpisode(client)

    def download(
        self,
        q: str,
        *,
        n: int = 6,
        type: str = DEFAULT_TYPE,  # noqa: A002
        ratings: str = "true",
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
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            "content/v2/discover/search",
            params={
                "q": q,
                "n": n,
                "type": type,
                "ratings": ratings,
                "locale": locale or self._client.locale,
            },
            headers={"referer": "https://www.crunchyroll.com/search"},
            log_id=log_id,
        )

    def download_and_parse(
        self,
        q: str,
        *,
        n: int = 6,
        type: str = DEFAULT_TYPE,  # noqa: A002
        ratings: str = "true",
        locale: str | None = None,
    ) -> SearchModel:
        """Downloads and parses the search file.

        An empty response returns a valid (empty) model.
        """
        return self.parse(
            self.download(
                q,
                n=n,
                type=type,
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
        for datum in data.data or []:
            if datum.type == field_type:
                return [
                    model.model_validate(item)
                    for item in self.original_input(datum.items)
                ]
        return []

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

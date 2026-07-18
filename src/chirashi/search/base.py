# TODO: Validate
"""Contains the SearchTypeEndpoint class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel

from chirashi.base_api_endpoint import BaseEndpoint

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SearchTypeEndpoint[T: GAPIBaseModel](BaseEndpoint[T]):
    """Base class to manage a search file with a specific type."""

    type: str

    def download(
        self,
        q: str,
        *,
        n: int = 100,
        ratings: str = "true",
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the search file.

        # Example episodes query: https://www.crunchyroll.com/search?f=episode&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            GET /content/v2/discover/search?q=%23COMPASS2.0+ANIMATION+PROJECT&n=100&type=episode&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/search?f=episode&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            Cookie: gzip
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            Priority: u=0
            TE: trailers

        # Example movie_listing query:
        https://www.crunchyroll.com/search?f=movie_listing&q=009-1%3A%20The%20End%20of%20the%20Beginning
            GET /content/v2/discover/search?q=009-1:+The+End+of+the+Beginning&n=100&type=movie_listing&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/search?f=movie_listing&q=009-1%3A%20The%20End%20of%20the%20Beginning
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            TE: trailers

        Example music query: https://www.crunchyroll.com/search?f=music&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            GET /content/v2/discover/search?q=%23COMPASS2.0+ANIMATION+PROJECT&n=100&type=music&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/search?f=music&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            Priority: u=0
            TE: trailers

        Example series query: https://www.crunchyroll.com/search?f=series&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            GET /content/v2/discover/search?q=%23COMPASS2.0+ANIMATION+PROJECT&n=100&type=series&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/search?f=series&q=%23COMPASS2.0%20ANIMATION%20PROJECT
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            Priority: u=0
            TE: trailers
        """
        return self._client.search.download(
            q=q,
            n=n,
            type=self.type,
            ratings=ratings,
            locale=locale,
        )

    def download_and_parse(
        self,
        q: str,
        *,
        n: int = 100,
        ratings: str = "true",
        locale: str | None = None,
    ) -> T:
        """Downloads and parses the search file.

        An empty response returns a valid (empty) model.
        """
        return self.parse(
            self.download(
                q=q,
                n=n,
                ratings=ratings,
                locale=locale,
            ),
        )

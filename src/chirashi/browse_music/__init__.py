# TODO: Validate
"""Contains the BrowseMusic class."""

from __future__ import annotations

from collections.abc import Sequence
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_music.models import BrowseMusicModel
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from chirashi.browse_music.models import Datum

logger = getLogger(__name__)
logger.addHandler(NullHandler())

N = 36


class BrowseMusic(BaseEndpoint[BrowseMusicModel]):
    """Manage the browse music file.

    The music catalogue is browsed by artist: every entry is a `musicArtist`,
    whose videos and concerts are then fetched per artist. Unlike the series
    browse this endpoint takes no `type` filter and only accepts
    `sort_by=newly_added`; anything else answers with a 400.

    Source: https://www.crunchyroll.com/music

    Example request:
        - GET /content/v2/music/browse?
            - n=36&
            - locale=en-US
            - HTTP/2
        - Host: www.crunchyroll.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Authorization: Bearer __REDACTED__
        - Sec-GPC: 1
        - Connection: keep-alive
        - Referer: https://www.crunchyroll.com/music
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = BrowseMusicModel

    @override
    def download(
        self,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, str | int] = {
            "n": n,
            "locale": locale or self._client.locale,
        }

        if start:
            params["start"] = start

        response = self._client.download(
            "content/v2/music/browse",
            params=params,
            headers={"referer": "https://www.crunchyroll.com/music"},
            log_id=log_id,
        )
        return self._validate_download(response, start)

    def _validate_download(
        self,
        response: dict[str, Any],
        start: int,
    ) -> dict[str, Any]:
        # A start past the end of the catalogue is answered with an empty page
        # and a total of 0 rather than an error, so it has to be caught here.
        total = response["total"]
        if start and start > total:
            raise StartOutOfRangeError(start, total, response)
        return response

    def download_all(
        self,
        *,
        n: int = N,
        locale: str | None = None,
    ) -> list[dict[str, Any]]:
        """Downloads every page of the music catalogue."""
        results: list[dict[str, Any]] = []
        start = 0

        while True:
            page = self.download(start=start, n=n, locale=locale)
            results.append(page)
            start += n
            if start >= page["total"]:
                return results

    @override
    def download_and_parse(
        self,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
    ) -> BrowseMusicModel:
        return self.parse(self.download(start=start, n=n, locale=locale))

    def download_and_parse_all(
        self,
        *,
        n: int = N,
        locale: str | None = None,
    ) -> list[BrowseMusicModel]:
        """Downloads and parses every page of the music catalogue."""
        return [self.parse(page) for page in self.download_all(n=n, locale=locale)]

    def extract_data(
        self,
        input_data: BrowseMusicModel
        | dict[str, Any]
        | Sequence[BrowseMusicModel | dict[str, Any]],
    ) -> list[Datum]:
        """Extracts data entries from one or more files."""
        responses = input_data if isinstance(input_data, Sequence) else [input_data]

        result: list[Datum] = []
        for response in responses:
            parsed = (
                response
                if isinstance(response, BrowseMusicModel)
                else self.parse(response)
            )
            result.extend(parsed.data)
        return result

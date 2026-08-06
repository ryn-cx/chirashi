# TODO: Validate
"""Contains the Artist class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from chirashi.artist.models import ArtistModel
from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ArtistNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Artist(BaseEndpoint[ArtistModel]):
    """Manage the artist file.

    Source: https://www.crunchyroll.com/artist/{artist_id}/{slug}

    Example request:
        - GET /content/v2/music/artists/{artist_id}?
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
        - Referer: https://www.crunchyroll.com/artist/{artist_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = ArtistModel

    @override
    def download(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint="content/v2/music/artists/" + artist_id,
                params={"locale": locale or self._client.locale},
                headers={"referer": f"https://www.crunchyroll.com/artist/{artist_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ArtistNotFoundError(
                artist_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> ArtistModel:
        return self.parse(self.download(artist_id, locale=locale))

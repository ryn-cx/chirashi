# TODO: Validate
"""Contains the Artist class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from chirashi.artist.models import ArtistModel, model_validate_json
from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import (
    ArtistNotFoundError,
    ChirashiError,
    ResourceNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_artist(response: str) -> dict[str, Any]:
    """Extract the artist from the Artist response."""
    if data := json.loads(response)["data"]:
        return data[0]

    msg = "The response has no artist in it"
    raise ChirashiError(msg)


class Artist(BaseEndpoint):
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

    # TODO: Validate
    def __call__(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> ArtistModel:
        """Download and parse the artist file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(artist_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the artist file."""
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

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ArtistModel:
        """Load a artist file into its model."""
        return model_validate_json(
            extract_artist(data),
            log_id or self.default_log_id,
        )

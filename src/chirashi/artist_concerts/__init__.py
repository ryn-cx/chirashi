# TODO: Validate
"""Contains the ArtistConcerts class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from chirashi.artist_concerts.models import ArtistConcertsModel, model_validate_json
from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ArtistNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class ArtistConcerts(BaseEndpoint):
    """Manage the artist concerts file.

    An artist with no concerts answers with a `total` of 0 rather than an error,
    so an empty response is a valid result and not a missing artist.

    Source: https://www.crunchyroll.com/artist/{artist_id}/{slug}

    Example request:
        - GET /content/v2/music/artists/{artist_id}/concerts?
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
    ) -> ArtistConcertsModel:
        """Look the artist concerts up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(artist_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the artist concerts file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint=f"content/v2/music/artists/{artist_id}/concerts",
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
    def load(self, data: str, log_id: str = "") -> ArtistConcertsModel:
        """Read a downloaded artist concerts file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

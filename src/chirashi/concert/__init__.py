# TODO: Validate
"""Contains the Concert class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.concert.models import ConcertModel, model_validate_json
from chirashi.exceptions import ConcertNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Concert(BaseEndpoint):
    """Manage the concert file.

    Source: https://www.crunchyroll.com/watch/concert/{concert_id}/{slug}

    Example request:
        - GET /content/v2/music/concerts/{concert_id}?
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
        - Referer: https://www.crunchyroll.com/watch/concert/{concert_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    # TODO: Validate
    def __call__(
        self,
        concert_id: str,
        *,
        locale: str | None = None,
    ) -> ConcertModel:
        """Look the concert up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(concert_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        concert_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the concert file."""
        log_id = self.get_log_id(self.download, locals())
        referer = f"https://www.crunchyroll.com/watch/concert/{concert_id}"
        try:
            return self._client.download(
                endpoint="content/v2/music/concerts/" + concert_id,
                params={"locale": locale or self._client.locale},
                headers={"referer": referer},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ConcertNotFoundError(
                concert_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ConcertModel:
        """Read a downloaded concert file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

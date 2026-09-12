# TODO: Validate
"""Contains the SimilarTo class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.similar_to.models import SimilarToModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

N = 30


# TODO: Validate
class SimilarTo(BaseEndpoint):
    """Manage the similar to file.

    A series with no recommendations, and a series id that does not exist, both
    answer with a `total` of 0 rather than an error.

    Source: https://www.crunchyroll.com/series/{series_id}/{slug}

    Example request:
        - GET /content/v2/discover/similar_to/{series_id}?
            - locale=en-US&
            - n=30&
            - ratings=true&
            - preferred_audio_language=ja-JP
            - HTTP/2
        - Host: www.crunchyroll.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Authorization: Bearer __REDACTED__
        - Connection: keep-alive
        - Referer: https://www.crunchyroll.com/series/{series_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    # TODO: Validate
    def __call__(
        self,
        series_id: str,
        *,
        n: int = N,
        ratings: str = "true",
        preferred_audio_language: str | None = None,
        locale: str | None = None,
    ) -> SimilarToModel:
        """Download and parse the similar to file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                n=n,
                ratings=ratings,
                preferred_audio_language=preferred_audio_language,
                locale=locale,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: str,
        *,
        n: int = N,
        ratings: str = "true",
        preferred_audio_language: str | None = None,
        locale: str | None = None,
    ) -> str:
        """Download the similar to file."""
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint=f"content/v2/discover/similar_to/{series_id}",
            params={
                "locale": locale or self._client.locale,
                "n": n,
                "ratings": ratings,
                "preferred_audio_language": preferred_audio_language,
            },
            headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SimilarToModel:
        """Load a similar to file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

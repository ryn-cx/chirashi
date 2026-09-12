# TODO: Validate
"""Contains the Categories class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.categories.models import CategoriesModel, model_validate_json
from chirashi.exceptions import ResourceNotFoundError, SeriesNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Categories(BaseEndpoint):
    """Manage the series categories file.

    Source: https://www.crunchyroll.com/series/{series_id}/{slug}

    Example request:
        - GET /content/v2/discover/categories?
            - guid={series_id}&
            - preferred_audio_language=ja-JP&
            - locale=en-US
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
        preferred_audio_language: str = "ja-JP",
        locale: str | None = None,
    ) -> CategoriesModel:
        """Download and parse the series categories file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
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
        preferred_audio_language: str = "ja-JP",
        locale: str | None = None,
    ) -> str:
        """Download the series categories file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint="content/v2/discover/categories",
                params={
                    "guid": series_id,
                    "preferred_audio_language": preferred_audio_language,
                    "locale": locale or self._client.locale,
                },
                headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(
                series_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, series_id)

    # TODO: Validate
    def _validate_download(self, response: str, series_id: str) -> str:
        """Check that the file holds categories.

        A series that does not exist is answered with an empty list rather than
        with an error.
        """
        if not json.loads(response).get("data"):
            raise SeriesNotFoundError(series_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CategoriesModel:
        """Load a series categories file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

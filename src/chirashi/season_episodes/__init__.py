"""Contains the SeasonEpisodes class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ResourceNotFoundError, SeasonEpisodesNotFoundError
from chirashi.season_episodes.models import SeasonEpisodesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SeasonEpisodes(BaseEndpoint[SeasonEpisodesModel]):
    """Manage the season episodes file.

    Source: https://www.crunchyroll.com/series/{series_id}/{slug}

    Example request:
        - GET /content/v2/cms/seasons/{season_id}/episodes?
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
        - Referer: https://www.crunchyroll.com/series/{series_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Priority: u=0
        - TE: trailers
    """

    _response_model = SeasonEpisodesModel

    @override
    def download(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v2/cms/seasons/{season_id}/episodes",
                params={"locale": locale or self._client.locale},
                headers={"referer": f"https://www.crunchyroll.com/series/{season_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonEpisodesNotFoundError(
                season_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, season_id)

    def _validate_download(
        self,
        response: dict[str, Any],
        season_id: str,
    ) -> dict[str, Any]:
        if not response.get("data"):
            raise SeasonEpisodesNotFoundError(season_id, HTTPStatus.OK, response)
        return response

    @override
    def download_and_parse(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> SeasonEpisodesModel:
        return self.parse(self.download(season_id, locale=locale))

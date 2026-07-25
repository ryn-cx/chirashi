"""Contains the Series class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ResourceNotFoundError, SeriesNotFoundError
from chirashi.series.models import SeriesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Series(BaseEndpoint[SeriesModel]):
    """Manage the series file.

    Source: https://www.crunchyroll.com/series/{series_id}/{slug}

    Example request:
        - GET /content/v2/cms/series/{series_id}?
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
        - TE: trailers
    """

    _response_model = SeriesModel

    @override
    def download(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint="content/v2/cms/series/" + series_id,
                params={"locale": locale or self._client.locale},
                headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(
                series_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> SeriesModel:
        return self.parse(self.download(series_id, locale=locale))

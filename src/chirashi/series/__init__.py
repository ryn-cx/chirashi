# TODO: Validate
"""Contains the Series class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.series.models import SeriesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Series(BaseEndpoint[SeriesModel]):
    """Manage the series file."""

    _response_model = SeriesModel

    def get_log_id(self, series_id: str, *, locale: str | None = None) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {series_id=}",
            locale=(locale, None),
        )

    def download(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the series file.

        Example request: https://www.crunchyroll.com/series/GEXH3W29Z/compass20-animation-project
            GET /content/v2/cms/series/GEXH3W29Z?locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/series/GEXH3W29Z/compass20-animation-project
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            TE: trailers
        """
        return self._client.download(
            endpoint="content/v2/cms/series/" + series_id,
            params={"locale": locale or self._client.locale},
            headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
            log_id=self.get_log_id(series_id, locale=locale),
        )

    def download_and_parse(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> SeriesModel:
        """Downloads and parses the series file.

        An empty response returns a valid (empty) model.
        """
        return self.parse(self.download(series_id, locale=locale))

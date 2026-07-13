# TODO: Validate
"""Contains the Series class."""

from __future__ import annotations

from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.series.models import SeriesModel


class Series(BaseEndpoint[SeriesModel]):
    """Manage the series file."""

    _response_model = SeriesModel

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
            log_id=f"{self.__class__.__name__} {series_id}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response["data"])

    def get(self, series_id: str, *, locale: str | None = None) -> SeriesModel:
        """Downloads and parses the series file."""
        data = self.download(series_id, locale=locale)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {series_id}")

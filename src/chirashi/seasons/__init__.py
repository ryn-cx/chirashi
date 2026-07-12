"""Contains the Seasons class."""

from __future__ import annotations

from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.seasons.models import Seasons as SeasonsModel


class Seasons(BaseEndpoint[SeasonsModel]):
    """Manage the seasons file."""

    _response_model = SeasonsModel

    def download(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the seasons file.

        Example request: https://www.crunchyroll.com/series/GEXH3W29Z/compass20-animation-project
            GET /content/v2/cms/series/GEXH3W29Z/seasons?force_locale=&preferred_audio_language=ja-JP&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/series/GEXH3W29Z/compass20-animation-project
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            If-None-Match: W/"53a-1CypegRfVUIgeWyid/fFF1pVOZw"
            Priority: u=6
            Cache-Control: max-age=0
            TE: trailers
        """
        return self._client.download(
            f"content/v2/cms/series/{series_id}/seasons",
            params={
                "locale": locale or self._client.locale,
                "force_locale": None,
            },
            headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
            log_id=f"{self.__class__.__name__} {series_id}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response["data"])

    def get(self, series_id: str, *, locale: str | None = None) -> SeasonsModel:
        """Downloads and parses the seasons file."""
        data = self.download(series_id, locale=locale)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {series_id}")

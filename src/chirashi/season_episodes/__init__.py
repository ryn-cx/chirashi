# TODO: Validate
"""Contains the SeasonEpisodes class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.season_episodes.models import SeasonEpisodesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SeasonEpisodes(BaseEndpoint[SeasonEpisodesModel]):
    """Manage the season episodes file."""

    _response_model = SeasonEpisodesModel

    def download(self, series_id: str, locale: str | None = None) -> dict[str, Any]:
        """Downloads the season episodes file.

        Example request: https://www.crunchyroll.com/series/GEXH3W29Z/compass20-animation-project
            GET /content/v2/cms/seasons/G68VCP0VQ/episodes?locale=en-US HTTP/2
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
            Priority: u=0
            TE: trailers
        """
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint=f"content/v2/cms/seasons/{series_id}/episodes",
            params={"locale": locale or self._client.locale},
            headers={"referer": f"https://www.crunchyroll.com/series/{series_id}"},
            log_id=log_id,
        )

    def download_and_parse(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> SeasonEpisodesModel:
        """Downloads and parses the season episodes file.

        An empty response returns a valid (empty) model.
        """
        return self.parse(self.download(series_id, locale=locale))

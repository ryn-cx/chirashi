"""Contains the SeasonEpisodes class."""

from __future__ import annotations

import re
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ResourceNotFoundError, SeasonNotFoundError
from chirashi.season_episodes.models import SeasonEpisodesModel, model_validate_json

if TYPE_CHECKING:
    from chirashi.season_episodes.models import Datum

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SeasonEpisodes(BaseEndpoint):
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

    # TODO: Validate
    def __call__(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> SeasonEpisodesModel:
        """Download and parse the season episodes file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(season_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the season episodes file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"content/v2/cms/seasons/{season_id}/episodes",
                params={"locale": locale or self._client.locale},
                headers={"referer": f"https://www.crunchyroll.com/series/{season_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(
                season_id,
                err.status_code,
                err.response,
            ) from err
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SeasonEpisodesModel:
        """Load a season episodes file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    @staticmethod
    def episode_number(episode: Datum) -> int | float | None:
        if re.fullmatch(r"\d+\.\d+", episode.episode):
            number = float(episode.episode)
            return int(number) if number.is_integer() else number
        return episode.episode_number

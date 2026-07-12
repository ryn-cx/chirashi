"""Contains the Chirashi class."""

import time
import uuid
from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from chirashi.browse_series import Browse
from chirashi.exceptions import HTTPError
from chirashi.search import Search
from chirashi.season_episodes import SeasonEpisodes
from chirashi.seasons import Seasons
from chirashi.series import Series

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DOMAIN = "beta-api.crunchyroll.com"


class Chirashi:
    """Crunchyroll API wrapper."""

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
    ) -> None:
        """Initialize the Chirashi client."""
        self.locale = locale
        self.get_around_client = get_around_client or GetAround()
        self.device_id = uuid.uuid4().hex
        # Chosen to match the (now deprecated?) Crunchyroll app on Windows.
        self.device_type = "Microsoft Edge on Windows"
        self._access_token_value = ""
        self._token_expires_at = datetime.now(tz=UTC)

        self.browse_series = Browse(self)
        self.series = Series(self)
        self.seasons = Seasons(self)
        self.season_episodes = SeasonEpisodes(self)
        self.search = Search(self)

    @property
    def _access_token(self) -> str:
        if not self._access_token_value or self._token_expires_at < datetime.now(UTC):
            self._download_access_token()
        return self._access_token_value

    def _download_access_token(self) -> None:
        url = f"https://{DOMAIN}/auth/v1/token"
        logger.debug("Downloading token:")
        start = time.monotonic()
        response = self.get_around_client.post(
            url,
            data={
                "device_id": self.device_id,
                "device_type": self.device_type,
                "grant_type": "client_id",
            },
            headers={"Authorization": "Basic bm9haWhkZXZtXzZpeWcwYThsMHE6"},
        )
        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        logger.debug("Downloaded token (%.4f s)", time.monotonic() - start)

        parsed = response.json()
        self._access_token_value = parsed["access_token"]
        self._token_expires_at = datetime.now(tz=UTC) + timedelta(
            seconds=parsed["expires_in"],
        )

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads from the API."""
        headers["authorization"] = f"Bearer {self._access_token}"

        logger.debug("Downloading: %s", log_id)
        url = f"https://{DOMAIN}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(url, params=params, headers=headers)

        if not response.is_success:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()

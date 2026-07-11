"""Crunchyroll API wrapper."""

import time
import uuid
from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from chirashi.browse_series import BrowseSeries
from chirashi.episodes import Episodes
from chirashi.exceptions import HTTPError
from chirashi.search import Search
from chirashi.seasons import Seasons
from chirashi.series import Series

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DOMAIN = "beta-api.crunchyroll.com"
# These values were chosen to match the Crunchyroll app on Windows.
DEVICE_ID = uuid.uuid4().hex
DEVICE_TYPE = "Microsoft Edge on Windows"


class Chirashi:
    """Crunchyroll API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the Chirashi client.

        Args:
            get_around_client: The HTTP client used for every request.
        """
        self.get_around_client = get_around_client or GetAround()
        self.device_id = DEVICE_ID
        self.device_type = DEVICE_TYPE
        self._access_token_value = ""
        self._token_expires_at = datetime.now(tz=UTC)

        self.browse_series = BrowseSeries(self)
        self.series = Series(self)
        self.seasons = Seasons(self)
        self.episodes = Episodes(self)
        self.search = Search(self)

    @property
    def _access_token(self) -> str:
        # Crunchyroll requires a bearer token even for anonymous access; fetch a
        # fresh anonymous token whenever the cached one is missing or expired.
        if not self._access_token_value or self._token_expires_at < datetime.now(
            tz=UTC,
        ):
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
        headers: dict[str, str] | None = None,
        log_id: object = None,
    ) -> dict[str, Any]:
        """Make a request to the Crunchyroll API with the given endpoint.

        Args:
            endpoint: The API path to request, relative to the Crunchyroll host.
            params: The query parameters for the request.
            headers: Optional request headers.
            log_id: An identifier for the request (e.g. the series or season ID)
                included in log messages to distinguish requests.

        Returns:
            The raw JSON response, suitable for passing to ``parse()``.

        Raises:
            HTTPError: If the response status code is not 200.
        """
        if headers is None:
            headers = {}
        headers["authorization"] = f"Bearer {self._access_token}"

        operation = f"{endpoint} ({log_id})"
        logger.debug("Downloading: %s", operation)
        url = f"https://{DOMAIN}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(url, params=params, headers=headers)

        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        logger.debug("Downloaded %s (%.4f s)", operation, time.monotonic() - start)

        return response.json()

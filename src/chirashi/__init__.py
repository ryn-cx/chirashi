"""Chirashi is a client for downloading and parsing data from Crunchyroll."""

import base64
import re
import uuid
from datetime import UTC, datetime, timedelta
from functools import cached_property
from logging import NullHandler, getLogger
from typing import Any

import requests

from chirashi.browse_series import BrowseSeries
from chirashi.episodes import Episodes
from chirashi.exceptions import HTTPError
from chirashi.seasons import Seasons
from chirashi.series import Series

DEVICE_ID = uuid.uuid4().hex
DEFAULT_TIMEOUT = 30

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Chirashi:
    """Interface for downloading and parsing data from Crunchyroll."""

    def __init__(
        self,
        username: str | None = None,
        password: str | None = None,
        # These values were chosen to match the CrunchyRoll app on Windows.
        device_id: str = DEVICE_ID,
        device_type: str = "Microsoft Edge on Windows",
        timeout: int = 30,
    ) -> None:
        """Initialize the Chirashi client."""
        self.timeout = timeout
        self.anonymous = not (username and password)
        self.username = username
        self.password = password
        self.__token_expires_at = datetime.now(tz=UTC)
        self.device_id = device_id
        self.device_type = device_type
        self.__access_token_value = ""
        self.__refresh_token = ""
        self.domain = "beta-api.crunchyroll.com"

        self.browse_series = BrowseSeries(self)
        self.series = Series(self)
        self.seasons = Seasons(self)
        self.episodes = Episodes(self)

        super().__init__()

    @cached_property
    def __public_token(self) -> str:
        """Get a public token from Crunchyroll.

        When accessing Crunchyroll through the web browser the token is obtained from
        https://www.crunchyroll.com/auth/v1/token but this endpoint has extra
        protection on it that makes it annoying to use. This This endpoint is used by
        the Windows Crunchyroll app and doesn't have the same protections, so it is
        much easier to use.
        """
        url = "https://static.crunchyroll.com/vilos-v2/web/vilos/js/bundle.js"
        logger.info("Downloading public token: %s", url)
        response = requests.get(url, timeout=self.timeout)
        response_text = response.text

        if not (match := re.search(r'prod="([\w-]+:[\w-]+)"', response_text)):
            msg = "Failed to extract token from bundle.js"
            raise ValueError(msg)

        encoded_public_token = match.group(1)
        return base64.b64encode(
            encoded_public_token.encode("iso-8859-1"),
        ).decode()

    @property
    def __access_token(self) -> str:
        if not self.__access_token_value or self.__token_expires_at < datetime.now(
            tz=UTC,
        ):
            self.__download_access_token()

        return self.__access_token_value

    @__access_token.setter
    def __access_token(self, value: str) -> None:
        self.__access_token_value = value

    def __download_access_token(self) -> None:
        url = f"https://{self.domain}/auth/v1/token"
        headers = {"Authorization": f"Basic {self.__public_token}"}

        data: dict[str, Any] = {
            "device_id": self.device_id,
            "device_type": self.device_type,
        }

        if self.__refresh_token:
            logger.info("Refreshing access token: %s", url)
            data["grant_type"] = "refresh_token"
            data["refresh_token"] = self.__refresh_token
        elif self.anonymous:
            logger.info("Downloading anonymous access token: %s", url)
            data["grant_type"] = "client_id"
        else:
            logger.info("Downloading logged in access token: %s", url)
            data["grant_type"] = "password"
            data["scope"] = "offline_access"
            data["username"] = self.username
            data["device_name"] = self.password

        response = requests.post(url, data, headers=headers, timeout=self.timeout)
        parsed_response = response.json()

        self.__access_token = parsed_response["access_token"]
        self.__token_expires_at = datetime.now(tz=UTC) + timedelta(
            seconds=parsed_response["expires_in"],
        )

        # Refresh token are only available when the user is logged into an account.
        if "refresh_token" in parsed_response:
            self.__refresh_token = parsed_response["refresh_token"]

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Make a request to the Crunchyroll API with the given endpoint."""
        if headers is None:
            headers = {}
        headers["authorization"] = f"Bearer {self.__access_token}"

        url = f"https://{self.domain}/{endpoint}"
        logger.info("Downloading API data: %s", url)
        response = requests.get(url, params, headers=headers, timeout=self.timeout)

        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        output = response.json()
        output["chirashi"] = {}
        output["chirashi"]["params"] = params
        headers.pop("authorization")
        output["chirashi"]["headers"] = headers
        output["chirashi"]["url"] = url
        output["chirashi"]["timestamp"] = (
            datetime.now().astimezone().isoformat().replace("+00:00", "Z")
        )

        return output

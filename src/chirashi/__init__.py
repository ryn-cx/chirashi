# TODO: Validate
"""Chirashi is a client for downloading and parsing data from Crunchyroll."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround

from chirashi.browse_series import BrowseSeries
from chirashi.episodes import Episodes
from chirashi.exceptions import HTTPError, LoginError
from chirashi.search import Search
from chirashi.seasons import Seasons
from chirashi.series import Series

if TYPE_CHECKING:
    import httpx

DEVICE_ID = uuid.uuid4().hex

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Chirashi:
    """Interface for downloading and parsing data from Crunchyroll."""

    def __init__(  # noqa: PLR0913
        self,
        username: str | None = None,
        password: str | None = None,
        # These values were chosen to match the CrunchyRoll app on Windows.
        device_id: str = DEVICE_ID,
        device_type: str = "Microsoft Edge on Windows",
        timeout: int = 30,
        get_around_server: str | None = None,
        get_around_password: str | None = None,
        # A previously obtained etp_rt cookie to reuse instead of logging in.
        etp_rt: str | None = None,
    ) -> None:
        """Initialize the Chirashi client."""
        self.get_around_client = GetAround(
            server=get_around_server,
            password=get_around_password,
        )
        self.timeout = timeout
        self.anonymous = not (username and password) and not etp_rt
        self.username = username
        self.password = password
        self._token_expires_at = datetime.now(tz=UTC)
        self.device_id = device_id
        self.device_type = device_type
        self._access_token_value = ""
        self._etp_rt = etp_rt or ""
        self.domain = "beta-api.crunchyroll.com"

        self.browse_series = BrowseSeries(self)
        self.series = Series(self)
        self.seasons = Seasons(self)
        self.episodes = Episodes(self)
        self.search = Search(self)

    @property
    def _access_token(self) -> str:
        if not self._access_token_value or self._token_expires_at < datetime.now(
            tz=UTC,
        ):
            self._download_access_token()

        return self._access_token_value

    @_access_token.setter
    def _access_token(self, value: str) -> None:
        self._access_token_value = value

    @property
    def etp_rt(self) -> str:
        """The etp_rt cookie."""
        return self._etp_rt

    @staticmethod
    def _cookies(response: httpx.Response) -> dict[str, str]:
        cookies: dict[str, str] = {}
        for raw in response.headers.get_list("set-cookie"):
            name, _, rest = raw.partition("=")
            cookies[name.strip()] = rest.split(";", 1)[0]
        return cookies

    def _login(self) -> str:
        base = "https://sso.crunchyroll.com"
        # A browser-like User-Agent is required for the SSO login flow.
        user_agent = (
            "Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0"
        )
        # The login endpoint only sets etp_rt when the Cloudflare __cf_bm cookie
        # from an initial page load is present, so warm up first to obtain it.
        warmup = self.get_around_client.get(
            f"{base}/login",
            headers={"User-Agent": user_agent},
            timeout=self.timeout,
        )
        cf_bm = self._cookies(warmup).get("__cf_bm", "")

        response = self.get_around_client.post(
            f"{base}/api/login",
            json={
                "email": self.username,
                "password": self.password,
                "eventSettings": {},
            },
            headers={
                "User-Agent": user_agent,
                "Origin": base,
                "Referer": f"{base}/login",
            },
            cookies={"__cf_bm": cf_bm, "device_id": self.device_id},
            timeout=self.timeout,
        )

        etp_rt = self._cookies(response).get("etp_rt")
        if not etp_rt:
            try:
                error = response.json().get("error", "Login failed")
            except ValueError, AttributeError:
                error = "Login failed"
            raise LoginError(error)
        return etp_rt

    def _download_access_token(self) -> None:
        if self.anonymous:
            self._store_access_token(self._request_token("client_id"))
        else:
            self._download_logged_in_access_token()

    def _download_logged_in_access_token(self) -> None:
        # Prefer the cached etp_rt; only log in when one isn't already available.
        logged_in = False
        if not self._etp_rt:
            self._etp_rt = self._login()
            logged_in = True

        parsed_response = self._request_etp_rt_token()

        # A cached etp_rt may have expired; fall back to a fresh login and retry.
        if "access_token" not in parsed_response and not logged_in:
            logger.info("Cached etp_rt rejected; logging in again.")
            self._etp_rt = self._login()
            parsed_response = self._request_etp_rt_token()

        self._store_access_token(parsed_response)

    def _request_etp_rt_token(self) -> dict[str, Any]:
        return self._request_token(
            "etp_rt_cookie",
            cookies={"device_id": self.device_id, "etp_rt": self._etp_rt},
        )

    def _request_token(
        self,
        grant_type: str,
        cookies: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        url = f"https://{self.domain}/auth/v1/token"
        logger.info("Downloading access token (%s): %s", grant_type, url)
        response = self.get_around_client.post(
            url,
            data={
                "device_id": self.device_id,
                "device_type": self.device_type,
                "grant_type": grant_type,
            },
            # TODO: How long is this token valid for?
            headers={"Authorization": "Basic bm9haWhkZXZtXzZpeWcwYThsMHE6"},
            cookies=cookies or {},
            timeout=self.timeout,
        )
        return response.json()

    def _store_access_token(self, parsed_response: dict[str, Any]) -> None:
        if "access_token" not in parsed_response:
            raise LoginError(parsed_response.get("error", "Login failed"))

        self._access_token = parsed_response["access_token"]
        self._token_expires_at = datetime.now(tz=UTC) + timedelta(
            seconds=parsed_response["expires_in"],
        )

    def login(self, username: str, password: str) -> None:
        """Log in with the given credentials.

        Args:
            username: The Crunchyroll username.
            password: The Crunchyroll password.

        Raises:
            LoginError: If the credentials are invalid.
        """
        self.username = username
        self.password = password
        self.anonymous = False
        self._access_token_value = ""
        self._etp_rt = ""
        self._download_access_token()

    def logout(self) -> None:
        """Log out and revert to anonymous access."""
        self.username = None
        self.password = None
        self.anonymous = True
        self._access_token_value = ""
        self._etp_rt = ""

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Make a request to the Crunchyroll API with the given endpoint."""
        if headers is None:
            headers = {}
        headers["authorization"] = f"Bearer {self._access_token}"

        url = f"https://{self.domain}/{endpoint}"
        logger.info("Downloading API data: %s", url)
        response = self.get_around_client.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

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

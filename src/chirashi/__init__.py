"""Contains the Chirashi class."""

import json
import time
import uuid
from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from chirashi.artist import Artist
from chirashi.artist_concerts import ArtistConcerts
from chirashi.artist_music_videos import ArtistMusicVideos
from chirashi.browse_music import BrowseMusic
from chirashi.browse_series import Browse
from chirashi.concert import Concert
from chirashi.exceptions import HTTPError, ResourceNotFoundError
from chirashi.music_video import MusicVideo
from chirashi.objects import Objects
from chirashi.search import Search
from chirashi.search.episode import SearchEpisode
from chirashi.search.movie_listing import SearchMovieListing
from chirashi.search.music import SearchMusic
from chirashi.search.series import SearchSeries
from chirashi.season_episodes import SeasonEpisodes
from chirashi.seasons import Seasons
from chirashi.series import Series

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# beta-api.crunchyroll.com has easier authorization, but it may be deprecated in the
# future.
API_DOMAIN = "beta-api.crunchyroll.com"


class Chirashi:
    """Crunchyroll API wrapper."""

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
    ) -> None:
        """Initializes the Chirashi client."""
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
        self.objects = Objects(self)
        self.search = Search(self)
        self.search_movie_listing = SearchMovieListing(self)
        self.search_series = SearchSeries(self)
        self.search_music = SearchMusic(self)
        self.search_episode = SearchEpisode(self)
        self.browse_music = BrowseMusic(self)
        self.music_video = MusicVideo(self)
        self.concert = Concert(self)
        self.artist = Artist(self)
        self.artist_music_videos = ArtistMusicVideos(self)
        self.artist_concerts = ArtistConcerts(self)

    @property
    def _access_token(self) -> str:
        if not self._access_token_value or self._token_expires_at < datetime.now(UTC):
            self._download_access_token()
        return self._access_token_value

    def _download_access_token(self) -> None:
        url = f"https://{API_DOMAIN}/auth/v1/token"
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
            raise HTTPError(response.status_code, response.text)

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
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(url, params=params, headers=headers)

        if response.status_code != HTTPStatus.OK:
            try:
                code = json.loads(response.text).get("code")
            except ValueError, AttributeError:
                code = None
            if isinstance(code, str) and code.endswith(".resource_not_found"):
                raise ResourceNotFoundError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()

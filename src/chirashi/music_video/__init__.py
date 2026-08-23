# TODO: Validate
"""Contains the MusicVideo class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import MusicVideoNotFoundError, ResourceNotFoundError
from chirashi.music_video.models import MusicVideoModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MusicVideo(BaseEndpoint):
    """Manage the music video file.

    Source: https://www.crunchyroll.com/watch/musicvideo/{music_video_id}/{slug}

    Example request:
        - GET /content/v2/music/music_videos/{music_video_id}?
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
        - Referer: https://www.crunchyroll.com/watch/musicvideo/{music_video_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    # TODO: Validate
    def __call__(
        self,
        music_video_id: str,
        *,
        locale: str | None = None,
    ) -> MusicVideoModel:
        """Look the music video up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(music_video_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        music_video_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the music video file."""
        log_id = self.get_log_id(self.download, locals())
        referer = f"https://www.crunchyroll.com/watch/musicvideo/{music_video_id}"
        try:
            return self._client.download(
                endpoint="content/v2/music/music_videos/" + music_video_id,
                params={"locale": locale or self._client.locale},
                headers={"referer": referer},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MusicVideoNotFoundError(
                music_video_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MusicVideoModel:
        """Read a downloaded music video file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

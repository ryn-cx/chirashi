# TODO: Validate
"""Contains the ArtistMusicVideos class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from chirashi.artist_music_videos.models import ArtistMusicVideosModel
from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import ArtistNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class ArtistMusicVideos(BaseEndpoint[ArtistMusicVideosModel]):
    """Manage the artist music videos file.

    Every music video by an artist, which is the list the artist page renders
    rather than the id-only `videos` field the artist file carries.

    Source: https://www.crunchyroll.com/artist/{artist_id}/{slug}

    Example request:
        - GET /content/v2/music/artists/{artist_id}/music_videos?
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
        - Referer: https://www.crunchyroll.com/artist/{artist_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = ArtistMusicVideosModel

    @override
    def download(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint=f"content/v2/music/artists/{artist_id}/music_videos",
                params={"locale": locale or self._client.locale},
                headers={"referer": f"https://www.crunchyroll.com/artist/{artist_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ArtistNotFoundError(
                artist_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(
        self,
        artist_id: str,
        *,
        locale: str | None = None,
    ) -> ArtistMusicVideosModel:
        return self.parse(self.download(artist_id, locale=locale))

# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import MusicVideoNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

# https://www.crunchyroll.com/watch/musicvideo/MV5ADCC418
MUSIC_VIDEO_IDS = [pytest.param("MV5ADCC418", id="casanova posse by ali")]


# TODO: Validate
@pytest.mark.parametrize("music_video_id", MUSIC_VIDEO_IDS)
def test_download(client: Chirashi, music_video_id: str) -> None:
    music_video = client.music_video(music_video_id)
    assert music_video.id == music_video_id
    assert music_video.title


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(MusicVideoNotFoundError):
        client.music_video.download("MV00000000")

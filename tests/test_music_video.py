# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import MusicVideoNotFoundError
from chirashi.music_video.models import MusicVideoModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

MUSIC_VIDEO_IDS = [
    # https://www.crunchyroll.com/watch/musicvideo/MV5ADCC418
    pytest.param("MV5ADCC418", id="casanova posse by ali"),
]


# TODO: Validate
class MusicVideoTest(RecordedEndpoint):
    MODEL = MusicVideoModel


# TODO: Validate
@pytest.mark.parametrize("music_video_id", MUSIC_VIDEO_IDS)
def test_download(client: Chirashi, music_video_id: str) -> None:
    MusicVideoTest.download_test(
        music_video_id,
        lambda: client.music_video.download(music_video_id),
    )


# TODO: Validate
@pytest.mark.parametrize("music_video_id", MUSIC_VIDEO_IDS)
def test_parse(music_video_id: str) -> None:
    MusicVideoTest.parse_test(music_video_id)


# TODO: Validate
@pytest.mark.parametrize(
    "music_video_id",
    [pytest.param("MV00000000", id="music video that does not exist")],
)
def test_download_invalid(client: Chirashi, music_video_id: str) -> None:
    MusicVideoTest.error_test(
        music_video_id,
        lambda: client.music_video.download(music_video_id),
        MusicVideoNotFoundError,
    )

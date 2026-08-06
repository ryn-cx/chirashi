from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import MusicVideoNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.music_video import MusicVideo

# https://www.crunchyroll.com/watch/musicvideo/MV5ADCC418
MUSIC_VIDEO_ID = "MV5ADCC418"
INVALID_MUSIC_VIDEO_ID = "MV00000000"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> MusicVideo:
    return client.music_video


def test_download(client: MusicVideo) -> None:
    download_and_save(client, MUSIC_VIDEO_ID, lambda: client.download(MUSIC_VIDEO_ID))


def test_parse(client: MusicVideo) -> None:
    data = parsed_json(client, MUSIC_VIDEO_ID)
    assert data.data[0].id == MUSIC_VIDEO_ID


def test_download_invalid(client: MusicVideo) -> None:
    assert_error(
        client,
        INVALID_MUSIC_VIDEO_ID,
        lambda: client.download(INVALID_MUSIC_VIDEO_ID),
        MusicVideoNotFoundError,
    )

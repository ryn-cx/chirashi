# TODO: Validate
"""Rebuilds MusicVideoModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

MUSIC_VIDEO_IDS = ["MV5ADCC418"]


# TODO: Validate
def generate_music_video(client: Chirashi) -> None:
    """Rebuild MusicVideoModel."""
    for music_video_id in MUSIC_VIDEO_IDS:
        download_if_missing(
            FILES_PATH,
            "MusicVideoModel",
            music_video_id,
            lambda music_video_id=music_video_id: client.music_video.download(
                music_video_id,
            ),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "MusicVideoModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_music_video(Chirashi(build_client_automatically()))

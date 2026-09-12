from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from chirashi import Chirashi
from chirashi.music_video import extract_music_video
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "MusicVideoModel"


# TODO: Validate
class MusicVideoId(RecordingId[Chirashi]):
    music_video_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.music_video.download(self.music_video_id)


MUSIC_VIDEO_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, MusicVideoId)


# TODO: Validate
def generate_music_video(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, MUSIC_VIDEO_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MusicVideoId, extract_music_video)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_music_video(Chirashi(build_client_automatically()))

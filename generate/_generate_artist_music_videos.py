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
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ArtistMusicVideosModel"


# TODO: Validate
class ArtistMusicVideosId(RecordingId[Chirashi]):
    artist_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.artist_music_videos.download(self.artist_id)


ARTIST_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ArtistMusicVideosId)


# TODO: Validate
def generate_artist_music_videos(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, ARTIST_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ArtistMusicVideosId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_artist_music_videos(Chirashi(build_client_automatically()))

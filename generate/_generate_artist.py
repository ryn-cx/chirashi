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
from chirashi.artist import extract_artist
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ArtistModel"


# TODO: Validate
class ArtistId(RecordingId[Chirashi]):
    artist_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.artist.download(self.artist_id)


ARTIST_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ArtistId)


# TODO: Validate
def generate_artist(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, ARTIST_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ArtistId, extract_artist)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_artist(Chirashi(build_client_automatically()))

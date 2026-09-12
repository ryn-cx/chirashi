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

MODEL_NAME = "ArtistConcertsModel"


# TODO: Validate
class ArtistConcertsId(RecordingId[Chirashi]):
    artist_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.artist_concerts.download(self.artist_id)


ARTIST_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ArtistConcertsId)


# TODO: Validate
def generate_artist_concerts(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, ARTIST_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ArtistConcertsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_artist_concerts(Chirashi(build_client_automatically()))

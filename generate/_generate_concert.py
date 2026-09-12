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
from chirashi.concert import extract_concert
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ConcertModel"


# TODO: Validate
class ConcertId(RecordingId[Chirashi]):
    concert_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.concert.download(self.concert_id)


CONCERT_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ConcertId)


# TODO: Validate
def generate_concert(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CONCERT_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ConcertId, extract_concert)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_concert(Chirashi(build_client_automatically()))

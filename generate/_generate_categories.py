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

MODEL_NAME = "CategoriesModel"


# TODO: Validate
class CategoriesId(RecordingId[Chirashi]):
    series_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.categories.download(self.series_id)


SERIES_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, CategoriesId)


# TODO: Validate
def generate_categories(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SERIES_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, CategoriesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_categories(Chirashi(build_client_automatically()))

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

MODEL_NAME = "BrowseSeriesModel"


# TODO: Validate
class BrowseSeriesId(RecordingId[Chirashi]):
    start: int

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.browse_series.download(start=self.start)


STARTS = load_ids(GENERATOR_PATHS, MODEL_NAME, BrowseSeriesId)


# TODO: Validate
def generate_browse_series(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, STARTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, BrowseSeriesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_browse_series(Chirashi(build_client_automatically()))

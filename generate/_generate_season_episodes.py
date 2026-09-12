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

MODEL_NAME = "SeasonEpisodesModel"


# TODO: Validate
class SeasonEpisodesId(RecordingId[Chirashi]):
    season_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.season_episodes.download(self.season_id)


SEASON_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, SeasonEpisodesId)


# TODO: Validate
def generate_season_episodes(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASON_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SeasonEpisodesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season_episodes(Chirashi(build_client_automatically()))

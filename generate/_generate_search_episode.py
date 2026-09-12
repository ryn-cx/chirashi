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
from chirashi.search.base import extract_results
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "SearchEpisodeModel"


# TODO: Validate
class SearchEpisodeId(RecordingId[Chirashi]):
    query: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.search_episode.download(self.query)


QUERIES = load_ids(GENERATOR_PATHS, MODEL_NAME, SearchEpisodeId)


# TODO: Validate
def generate_search_episode(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, QUERIES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SearchEpisodeId, extract_results)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_episode(Chirashi(build_client_automatically()))

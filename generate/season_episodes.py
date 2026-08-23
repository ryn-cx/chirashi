# TODO: Validate
"""Rebuilds SeasonEpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

SEASON_IDS = [
    "G68VCP0VQ",
    "GRJQC18W2",
]


# TODO: Validate
def generate_season_episodes(client: Chirashi) -> None:
    """Rebuild SeasonEpisodesModel."""
    for season_id in SEASON_IDS:
        download_if_missing(
            FILES_PATH,
            "SeasonEpisodesModel",
            season_id,
            lambda season_id=season_id: client.season_episodes.download(season_id),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "SeasonEpisodesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season_episodes(Chirashi(build_client_automatically()))

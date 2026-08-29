# TODO: Validate
"""Rebuilds SeasonEpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

SEASON_IDS = load_ids("SeasonEpisodesModel")


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
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "SeasonEpisodesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season_episodes(Chirashi(build_client_automatically()))

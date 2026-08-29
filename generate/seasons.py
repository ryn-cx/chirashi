# TODO: Validate
"""Rebuilds SeasonsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

SERIES_IDS = load_ids("SeasonsModel")


# TODO: Validate
def generate_seasons(client: Chirashi) -> None:
    """Rebuild SeasonsModel."""
    for series_id in SERIES_IDS:
        download_if_missing(
            FILES_PATH,
            "SeasonsModel",
            series_id,
            lambda series_id=series_id: client.seasons.download(series_id),
        )
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "SeasonsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_seasons(Chirashi(build_client_automatically()))

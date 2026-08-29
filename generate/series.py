# TODO: Validate
"""Rebuilds SeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

SERIES_IDS = load_ids("SeriesModel")


# TODO: Validate
def generate_series(client: Chirashi) -> None:
    """Rebuild SeriesModel."""
    for series_id in SERIES_IDS:
        download_if_missing(
            FILES_PATH,
            "SeriesModel",
            series_id,
            lambda series_id=series_id: client.series.download(series_id),
        )
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "SeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_series(Chirashi(build_client_automatically()))

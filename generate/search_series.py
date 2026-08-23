# TODO: Validate
"""Rebuilds SearchSeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

QUERIES = ["#COMPASS2.0 ANIMATION PROJECT"]


# TODO: Validate
def generate_search_series(client: Chirashi) -> None:
    """Rebuild SearchSeriesModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchSeriesModel",
            query,
            lambda query=query: client.search_series.download(query),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "SearchSeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_series(Chirashi(build_client_automatically()))

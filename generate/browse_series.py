# TODO: Validate
"""Rebuilds BrowseSeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

STARTS = [0, 36, 72]
"""Where each recorded page of the catalogue starts."""


# TODO: Validate
def generate_browse_series(client: Chirashi) -> None:
    """Rebuild BrowseSeriesModel."""
    for start in STARTS:
        download_if_missing(
            FILES_PATH,
            "BrowseSeriesModel",
            start,
            lambda start=start: client.browse_series.download(start=start),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "BrowseSeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_browse_series(Chirashi(build_client_automatically()))

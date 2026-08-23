# TODO: Validate
"""Rebuilds BrowseMusicModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

STARTS = [
    0,
    36,
    72,
    108,
    144,
    180,
    216,
    252,
    288,
    324,
    360,
    396,
    432,
    468,
    504,
    540,
    576,
    612,
]
"""Where each recorded page of the catalogue starts."""


# TODO: Validate
def generate_browse_music(client: Chirashi) -> None:
    """Rebuild BrowseMusicModel."""
    for start in STARTS:
        download_if_missing(
            FILES_PATH,
            "BrowseMusicModel",
            start,
            lambda start=start: client.browse_music.download(start=start),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "BrowseMusicModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_browse_music(Chirashi(build_client_automatically()))

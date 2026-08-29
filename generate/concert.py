# TODO: Validate
"""Rebuilds ConcertModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

CONCERT_IDS = load_ids("ConcertModel")


# TODO: Validate
def generate_concert(client: Chirashi) -> None:
    """Rebuild ConcertModel."""
    for concert_id in CONCERT_IDS:
        download_if_missing(
            FILES_PATH,
            "ConcertModel",
            concert_id,
            lambda concert_id=concert_id: client.concert.download(concert_id),
        )
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "ConcertModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_concert(Chirashi(build_client_automatically()))

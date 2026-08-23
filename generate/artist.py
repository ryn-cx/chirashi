# TODO: Validate
"""Rebuilds ArtistModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

ARTIST_IDS = ["MA36EDC261"]


# TODO: Validate
def generate_artist(client: Chirashi) -> None:
    """Rebuild ArtistModel."""
    for artist_id in ARTIST_IDS:
        download_if_missing(
            FILES_PATH,
            "ArtistModel",
            artist_id,
            lambda artist_id=artist_id: client.artist.download(artist_id),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "ArtistModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_artist(Chirashi(build_client_automatically()))

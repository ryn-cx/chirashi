# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing

QUERIES = [
    "#COMPASS2.0 ANIMATION PROJECT",
    "009-1: The End of the Beginning",
    "CASANOVA POSSE",
    "This Is #COMPASS2.0",
    "zzzzzzzzzzzzzzzzzzzz",
]


# TODO: Validate
def generate_search(client: Chirashi) -> None:
    """Rebuild SearchModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            query,
            lambda query=query: client.search.download(query),
        )
    generate_model(FILES_PATH, CHIRASHI_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Chirashi(build_client_automatically()))

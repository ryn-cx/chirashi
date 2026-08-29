# TODO: Validate
"""Rebuilds SearchMovieListingModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

QUERIES = load_ids("SearchMovieListingModel")


# TODO: Validate
def generate_search_movie_listing(client: Chirashi) -> None:
    """Rebuild SearchMovieListingModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchMovieListingModel",
            query,
            lambda query=query: client.search_movie_listing.download(query),
        )
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "SearchMovieListingModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_movie_listing(Chirashi(build_client_automatically()))

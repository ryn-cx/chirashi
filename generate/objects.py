# TODO: Validate
"""Rebuilds ObjectsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from chirashi import Chirashi
from generate.constants import CHIRASHI_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

OBJECT_IDS = load_ids("ObjectsModel")


# TODO: Validate
def generate_objects(client: Chirashi) -> None:
    """Rebuild ObjectsModel."""
    for object_id in OBJECT_IDS:
        download_if_missing(
            FILES_PATH,
            "ObjectsModel",
            object_id,
            lambda object_id=object_id: client.objects.download(object_id),
        )
    rebuild_model(FILES_PATH, CHIRASHI_PATH, "ObjectsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_objects(Chirashi(build_client_automatically()))

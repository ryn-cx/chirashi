from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from chirashi import Chirashi
from chirashi.objects import extract_object
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ObjectsModel"


# TODO: Validate
class ObjectsId(RecordingId[Chirashi]):
    object_id: str

    # TODO: Validate
    def download(self, client: Chirashi) -> str:
        return client.objects.download(self.object_id)


OBJECT_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, ObjectsId)


# TODO: Validate
def generate_objects(client: Chirashi) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, OBJECT_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ObjectsId, extract_object)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_objects(Chirashi(build_client_automatically()))

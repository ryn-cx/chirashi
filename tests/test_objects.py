from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import EpisodeNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.objects import Objects

OBJECT_IDS = ["GE00258180JAJP"]
INVALID_OBJECT_ID = "GGGGGGGGGGGGG"


@pytest.fixture(scope="session")
def client(client: Chirashi) -> Objects:
    return client.objects


@pytest.mark.parametrize("object_id", OBJECT_IDS)
def test_download(client: Objects, object_id: str) -> None:
    download_and_save(client, object_id, lambda: client.download(object_id))


@pytest.mark.parametrize("object_id", OBJECT_IDS)
def test_parse(client: Objects, object_id: str) -> None:
    data = parsed_json(client, object_id)
    assert data.data[0].id == object_id


def test_download_invalid(client: Objects) -> None:
    assert_error(
        client,
        INVALID_OBJECT_ID,
        lambda: client.download(INVALID_OBJECT_ID),
        EpisodeNotFoundError,
    )

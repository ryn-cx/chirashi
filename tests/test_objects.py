# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import EpisodeNotFoundError
from chirashi.objects.models import ObjectsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi

OBJECT_IDS = [
    pytest.param("GE00258180JAJP", id="the magic that started everything"),
]


# TODO: Validate
class ObjectsTest(RecordedEndpoint):
    MODEL = ObjectsModel


# TODO: Validate
@pytest.mark.parametrize("object_id", OBJECT_IDS)
def test_download(client: Chirashi, object_id: str) -> None:
    ObjectsTest.download_test(object_id, lambda: client.objects.download(object_id))


# TODO: Validate
@pytest.mark.parametrize("object_id", OBJECT_IDS)
def test_parse(object_id: str) -> None:
    ObjectsTest.parse_test(object_id)


# TODO: Validate
@pytest.mark.parametrize(
    "object_id",
    [pytest.param("GGGGGGGGGGGGG", id="episode that does not exist")],
)
def test_download_invalid(client: Chirashi, object_id: str) -> None:
    ObjectsTest.error_test(
        object_id,
        lambda: client.objects.download(object_id),
        EpisodeNotFoundError,
    )

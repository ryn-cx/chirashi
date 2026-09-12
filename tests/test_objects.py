# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import EpisodeNotFoundError

if TYPE_CHECKING:
    from chirashi import Chirashi

OBJECT_IDS = [pytest.param("GE00258180JAJP", id="the magic that started everything")]


# TODO: Validate
@pytest.mark.parametrize("object_id", OBJECT_IDS)
def test_download(client: Chirashi, object_id: str) -> None:
    episode = client.objects(object_id)
    assert episode.id == object_id
    assert episode.title


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    with pytest.raises(EpisodeNotFoundError):
        client.objects.download("GGGGGGGGGGGGG")

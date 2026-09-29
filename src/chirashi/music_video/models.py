# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MusicVideoModel as OptionalModel
from .strict_models import MusicVideoModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artist,
        Artists,
        Availability,
        Genre,
        Images,
        MainArtistItem,
        MusicVideoModel,
        ThumbnailItem,
    )
else:
    from .optional_models import (
        Artist,
        Artists,
        Availability,
        Genre,
        Images,
        MainArtistItem,
        MusicVideoModel,
        ThumbnailItem,
    )

__all__ = [
    "Artist",
    "Artists",
    "Availability",
    "Genre",
    "Images",
    "MainArtistItem",
    "MusicVideoModel",
    "ThumbnailItem",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MusicVideoModel:
    """Read a downloaded file into MusicVideoModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ConcertModel as OptionalModel
from .strict_models import ConcertModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artist,
        Artists,
        Availability,
        ConcertModel,
        Genre,
        Images,
        MainArtistItem,
        ThumbnailItem,
    )
else:
    from .optional_models import (
        Artist,
        Artists,
        Availability,
        ConcertModel,
        Genre,
        Images,
        MainArtistItem,
        ThumbnailItem,
    )

__all__ = [
    "Artist",
    "Artists",
    "Availability",
    "ConcertModel",
    "Genre",
    "Images",
    "MainArtistItem",
    "ThumbnailItem",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ConcertModel:
    """Read a downloaded file into ConcertModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

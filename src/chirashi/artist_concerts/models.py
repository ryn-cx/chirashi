# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ArtistConcertsModel as OptionalModel
from .strict_models import ArtistConcertsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Artist,
        ArtistConcertsModel,
        Artists,
        Availability,
        Datum,
        Genre,
        Images,
        MainArtistItem,
        ThumbnailItem,
    )
else:
    from .optional_models import (
        Artist,
        ArtistConcertsModel,
        Artists,
        Availability,
        Datum,
        Genre,
        Images,
        MainArtistItem,
        ThumbnailItem,
    )

__all__ = [
    "Artist",
    "ArtistConcertsModel",
    "Artists",
    "Availability",
    "Datum",
    "Genre",
    "Images",
    "MainArtistItem",
    "ThumbnailItem",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ArtistConcertsModel:
    """Read a downloaded file into ArtistConcertsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

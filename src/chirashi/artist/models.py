# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ArtistModel as OptionalModel
from .strict_models import ArtistModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ArtistModel,
        Genre,
        Images,
        PosterTallItem,
        PosterWideItem,
    )
else:
    from .optional_models import (
        ArtistModel,
        Genre,
        Images,
        PosterTallItem,
        PosterWideItem,
    )

__all__ = [
    "ArtistModel",
    "Genre",
    "Images",
    "PosterTallItem",
    "PosterWideItem",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ArtistModel:
    """Read a downloaded file into ArtistModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

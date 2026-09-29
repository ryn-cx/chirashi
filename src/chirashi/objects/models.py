# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ObjectsModel as OptionalModel
from .strict_models import ObjectsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AdBreak,
        ContentDescriptorsWithSymbolItem,
        Down,
        EpisodeMetadata,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        ObjectsModel,
        Rating,
        ThumbnailItem,
        Up,
        Version,
    )
else:
    from .optional_models import (
        AdBreak,
        ContentDescriptorsWithSymbolItem,
        Down,
        EpisodeMetadata,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        ObjectsModel,
        Rating,
        ThumbnailItem,
        Up,
        Version,
    )

__all__ = [
    "AdBreak",
    "ContentDescriptorsWithSymbolItem",
    "Down",
    "EpisodeMetadata",
    "ExtendedMaturityRating",
    "Images",
    "LanguagePresentation",
    "LocalizedImages",
    "ObjectsModel",
    "Rating",
    "ThumbnailItem",
    "Up",
    "Version",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ObjectsModel:
    """Read a downloaded file into ObjectsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

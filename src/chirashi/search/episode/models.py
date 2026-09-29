# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchEpisodeModel as OptionalModel
from .strict_models import SearchEpisodeModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AdBreak,
        ContentDescriptorsWithSymbolItem,
        Down,
        EpisodeMetadata,
        ExtendedMaturityRating,
        Images,
        Item,
        LanguagePresentation,
        LocalizedImages,
        Rating,
        SearchEpisodeModel,
        SearchMetadata,
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
        Item,
        LanguagePresentation,
        LocalizedImages,
        Rating,
        SearchEpisodeModel,
        SearchMetadata,
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
    "Item",
    "LanguagePresentation",
    "LocalizedImages",
    "Rating",
    "SearchEpisodeModel",
    "SearchMetadata",
    "ThumbnailItem",
    "Up",
    "Version",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchEpisodeModel:
    """Read a downloaded file into SearchEpisodeModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

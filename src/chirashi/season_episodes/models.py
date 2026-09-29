# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SeasonEpisodesModel as OptionalModel
from .strict_models import SeasonEpisodesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AdBreak,
        ContentDescriptorsWithSymbolItem,
        Datum,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        Meta,
        SeasonEpisodesModel,
        ThumbnailItem,
        Version,
    )
else:
    from .optional_models import (
        AdBreak,
        ContentDescriptorsWithSymbolItem,
        Datum,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        Meta,
        SeasonEpisodesModel,
        ThumbnailItem,
        Version,
    )

__all__ = [
    "AdBreak",
    "ContentDescriptorsWithSymbolItem",
    "Datum",
    "ExtendedMaturityRating",
    "Images",
    "LanguagePresentation",
    "LocalizedImages",
    "Meta",
    "SeasonEpisodesModel",
    "ThumbnailItem",
    "Version",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SeasonEpisodesModel:
    """Read a downloaded file into SeasonEpisodesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

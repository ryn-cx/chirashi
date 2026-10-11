# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SimilarToModel as OptionalModel
from .strict_models import SimilarToModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AdBreak,
        Award,
        ContentDescriptorsWithSymbolItem,
        Datum,
        Down,
        EpisodeMetadata,
        ExtendedMaturityRating,
        Field1s,
        Field2s,
        Field3s,
        Field4s,
        Field5s,
        Images,
        Images1,
        LanguagePresentation,
        Livestream,
        PosterTallItem,
        PosterWideItem,
        PromoImageItem,
        Rating,
        SearchMetadata,
        SeriesMetadata,
        SimilarToModel,
        ThumbnailItem,
        Up,
        Version,
    )
else:
    from .optional_models import (
        AdBreak,
        Award,
        ContentDescriptorsWithSymbolItem,
        Datum,
        Down,
        EpisodeMetadata,
        ExtendedMaturityRating,
        Field1s,
        Field2s,
        Field3s,
        Field4s,
        Field5s,
        Images,
        Images1,
        LanguagePresentation,
        Livestream,
        PosterTallItem,
        PosterWideItem,
        PromoImageItem,
        Rating,
        SearchMetadata,
        SeriesMetadata,
        SimilarToModel,
        ThumbnailItem,
        Up,
        Version,
    )

__all__ = [
    "AdBreak",
    "Award",
    "ContentDescriptorsWithSymbolItem",
    "Datum",
    "Down",
    "EpisodeMetadata",
    "ExtendedMaturityRating",
    "Field1s",
    "Field2s",
    "Field3s",
    "Field4s",
    "Field5s",
    "Images",
    "Images1",
    "LanguagePresentation",
    "Livestream",
    "PosterTallItem",
    "PosterWideItem",
    "PromoImageItem",
    "Rating",
    "SearchMetadata",
    "SeriesMetadata",
    "SimilarToModel",
    "ThumbnailItem",
    "Up",
    "Version",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SimilarToModel:
    """Read a downloaded file into SimilarToModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

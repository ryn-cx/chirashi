# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchSeriesModel as OptionalModel
from .strict_models import SearchSeriesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        ExtendedMaturityRating,
        Field1s,
        Field2s,
        Field3s,
        Field4s,
        Field5s,
        Images,
        Item,
        LanguagePresentation,
        LocalizedImages,
        PosterTallItem,
        PosterWideItem,
        PromoImageItem,
        Rating,
        SearchMetadata,
        SearchSeriesModel,
        SeriesMetadata,
    )
else:
    from .optional_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        ExtendedMaturityRating,
        Field1s,
        Field2s,
        Field3s,
        Field4s,
        Field5s,
        Images,
        Item,
        LanguagePresentation,
        LocalizedImages,
        PosterTallItem,
        PosterWideItem,
        PromoImageItem,
        Rating,
        SearchMetadata,
        SearchSeriesModel,
        SeriesMetadata,
    )

__all__ = [
    "Award",
    "ContentDescriptorsWithSymbolItem",
    "ExtendedMaturityRating",
    "Field1s",
    "Field2s",
    "Field3s",
    "Field4s",
    "Field5s",
    "Images",
    "Item",
    "LanguagePresentation",
    "LocalizedImages",
    "PosterTallItem",
    "PosterWideItem",
    "PromoImageItem",
    "Rating",
    "SearchMetadata",
    "SearchSeriesModel",
    "SeriesMetadata",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchSeriesModel:
    """Read a downloaded file into SearchSeriesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SeriesModel as OptionalModel
from .strict_models import SeriesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        PosterTallItem,
        PosterWideItem,
        SeriesModel,
    )
else:
    from .optional_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        ExtendedMaturityRating,
        Images,
        LanguagePresentation,
        LocalizedImages,
        PosterTallItem,
        PosterWideItem,
        SeriesModel,
    )

__all__ = [
    "Award",
    "ContentDescriptorsWithSymbolItem",
    "ExtendedMaturityRating",
    "Images",
    "LanguagePresentation",
    "LocalizedImages",
    "PosterTallItem",
    "PosterWideItem",
    "SeriesModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SeriesModel:
    """Read a downloaded file into SeriesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

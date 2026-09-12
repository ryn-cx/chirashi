"""SimilarToModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SimilarToModel as OptionalModel
from .strict_models import SimilarToModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        Datum,
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
    )
else:
    from .optional_models import (
        Award,
        ContentDescriptorsWithSymbolItem,
        Datum,
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
    )

__all__ = [
    "Award",
    "ContentDescriptorsWithSymbolItem",
    "Datum",
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
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SimilarToModel:
    """Read a downloaded file into SimilarToModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SeasonsModel as OptionalModel
from .strict_models import SeasonsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ContentDescriptorsWithSymbolItem,
        Datum,
        ExtendedMaturityRating,
        Meta,
        SeasonsModel,
        Version,
    )
else:
    from .optional_models import (
        ContentDescriptorsWithSymbolItem,
        Datum,
        ExtendedMaturityRating,
        Meta,
        SeasonsModel,
        Version,
    )

__all__ = [
    "ContentDescriptorsWithSymbolItem",
    "Datum",
    "ExtendedMaturityRating",
    "Meta",
    "SeasonsModel",
    "Version",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SeasonsModel:
    """Read a downloaded file into SeasonsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)

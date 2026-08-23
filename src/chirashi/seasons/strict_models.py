from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel
from typing import Any

class ExtendedMaturityRating(BaseModel):
    system: str
    rating: str
    level: str

class ContentDescriptorsWithSymbolItem(BaseModel):
    label: str

class Version(BaseModel):
    audio_locale: str
    guid: str
    original: bool
    variant: str

class Datum(BaseModel):
    id: str
    channel_id: str
    title: str
    slug_title: str
    series_id: str
    season_display_number: str
    season_sequence_number: int
    season_number: int
    is_complete: bool
    description: str
    keywords: list[str]
    season_tags: list[str]
    images: dict[str, Any]
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem]
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    seo_title: str
    seo_description: str
    availability_notes: str
    audio_locales: list[str]
    subtitle_locales: list[str]
    audio_locale: str
    versions: list[Version]
    identifier: str
    number_of_episodes: int

class Meta(BaseModel):
    versions_considered: bool | None = None

class SeasonsModel(BaseModel):
    data: list[Datum]
    meta: Meta
    total: int
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input

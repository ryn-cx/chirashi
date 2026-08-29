from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from typing import Any

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | None = None
    rating: str | None = None
    level: str | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | None = None
    guid: str | None = None
    original: bool | None = None
    variant: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    channel_id: str | None = None
    title: str | None = None
    slug_title: str | None = None
    series_id: str | None = None
    season_display_number: str | None = None
    season_sequence_number: int | None = None
    season_number: int | None = None
    is_complete: bool | None = None
    description: str | None = None
    keywords: list[str] | None = None
    season_tags: list[str] | None = None
    images: dict[str, Any] | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    maturity_ratings: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_simulcast: bool | None = None
    seo_title: str | None = None
    seo_description: str | None = None
    availability_notes: str | None = None
    audio_locales: list[str] | None = None
    subtitle_locales: list[str] | None = None
    audio_locale: str | None = None
    versions: list[Version] | None = None
    identifier: str | None = None
    number_of_episodes: int | None = None

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    versions_considered: bool | None = None

class SeasonsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | None = None
    meta: Meta | None = None
    total: int | None = None
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

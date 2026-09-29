from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from typing import Any

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    level: str | Any = Field(default=None, union_mode='left_to_right')

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    guid: str | Any = Field(default=None, union_mode='left_to_right')
    original: bool | Any = Field(default=None, union_mode='left_to_right')
    variant: str | Any = Field(default=None, union_mode='left_to_right')

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    channel_id: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    series_id: str | Any = Field(default=None, union_mode='left_to_right')
    season_display_number: str | Any = Field(default=None, union_mode='left_to_right')
    season_sequence_number: int | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    is_complete: bool | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    keywords: list[str] | Any = Field(default=None, union_mode='left_to_right')
    season_tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    images: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    extended_maturity_rating: ExtendedMaturityRating | Any = Field(default=None, union_mode='left_to_right')
    maturity_ratings: list[str] | Any = Field(default=None, union_mode='left_to_right')
    is_mature: bool | Any = Field(default=None, union_mode='left_to_right')
    mature_blocked: bool | Any = Field(default=None, union_mode='left_to_right')
    is_subbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_dubbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_simulcast: bool | Any = Field(default=None, union_mode='left_to_right')
    seo_title: str | Any = Field(default=None, union_mode='left_to_right')
    seo_description: str | Any = Field(default=None, union_mode='left_to_right')
    availability_notes: str | Any = Field(default=None, union_mode='left_to_right')
    audio_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    subtitle_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    versions: list[Version] | Any = Field(default=None, union_mode='left_to_right')
    identifier: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_episodes: int | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | Any = Field(default=None, union_mode='left_to_right')

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    versions_considered: bool | Any = Field(default=None, union_mode='left_to_right')

class SeasonsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')
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

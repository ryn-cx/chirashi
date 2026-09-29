from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import AwareDatetime, BaseModel, ConfigDict
from typing import Any

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: list[list[ThumbnailItem]] | Any = Field(default=None, union_mode='left_to_right')

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: str | Any = Field(default=None, union_mode='left_to_right')

class AdBreak(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    offset_ms: int | Any = Field(default=None, union_mode='left_to_right')

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    level: str | Any = Field(default=None, union_mode='left_to_right')
    advisories: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    guid: str | Any = Field(default=None, union_mode='left_to_right')
    original: bool | Any = Field(default=None, union_mode='left_to_right')
    variant: str | Any = Field(default=None, union_mode='left_to_right')
    season_guid: str | Any = Field(default=None, union_mode='left_to_right')
    media_guid: str | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation: str | Any = Field(default=None, union_mode='left_to_right')
    text_locale: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')
    is_original_audio: bool | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    audio_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_id: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(default=None, union_mode='left_to_right')
    series_slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_id: str | Any = Field(default=None, union_mode='left_to_right')
    season_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode: str | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(default=None, union_mode='left_to_right')
    season_display_number: str | Any = Field(default=None, union_mode='left_to_right')
    season_sequence_number: int | Any = Field(default=None, union_mode='left_to_right')
    duration_ms: int | Any = Field(default=None, union_mode='left_to_right')
    ad_breaks: list[AdBreak] | Any = Field(default=None, union_mode='left_to_right')
    episode_air_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    upload_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    availability_starts: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    availability_ends: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    eligible_region: str | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(default=None, union_mode='left_to_right')
    extended_maturity_rating: ExtendedMaturityRating | Any = Field(default=None, union_mode='left_to_right')
    maturity_ratings: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | Any = Field(default=None, union_mode='left_to_right')
    is_mature: bool | Any = Field(default=None, union_mode='left_to_right')
    mature_blocked: bool | Any = Field(default=None, union_mode='left_to_right')
    available_date: Any | None = None
    free_available_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    premium_date: Any | None = None
    premium_available_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    is_subbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_dubbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_clip: bool | Any = Field(default=None, union_mode='left_to_right')
    available_offline: bool | Any = Field(default=None, union_mode='left_to_right')
    linked_guid: str | Any = Field(default=None, union_mode='left_to_right')
    tenant_categories: list[str] | Any = Field(default=None, union_mode='left_to_right')
    subtitle_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    availability_notes: str | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    versions: list[Version] | Any = Field(default=None, union_mode='left_to_right')
    closed_captions_available: bool | Any = Field(default=None, union_mode='left_to_right')
    identifier: str | Any = Field(default=None, union_mode='left_to_right')
    availability_status: str | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    language_presentation: LanguagePresentation | Any = Field(default=None, union_mode='left_to_right')

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    score: float | Any = Field(default=None, union_mode='left_to_right')
    rank: int | Any = Field(default=None, union_mode='left_to_right')
    popularity_score: int | Any = Field(default=None, union_mode='left_to_right')

class Up(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Down(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    up: Up | Any = Field(default=None, union_mode='left_to_right')
    down: Down | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    external_id: str | Any = Field(default=None, union_mode='left_to_right')
    channel_id: str | Any = Field(default=None, union_mode='left_to_right')
    linked_resource_key: str | Any = Field(default=None, union_mode='left_to_right')
    new: bool | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    promo_title: str | Any = Field(default=None, union_mode='left_to_right')
    promo_description: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    localized_images: LocalizedImages | Any = Field(default=None, union_mode='left_to_right')
    episode_metadata: EpisodeMetadata | Any = Field(default=None, union_mode='left_to_right')
    search_metadata: SearchMetadata | Any = Field(default=None, union_mode='left_to_right')
    language_presentation: LanguagePresentation | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')

class SearchEpisodeModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')
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

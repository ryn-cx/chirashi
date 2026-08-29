from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict
from typing import Any

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: list[list[ThumbnailItem]] | None = None

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: str | None = None

class AdBreak(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    offset_ms: int | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | None = None
    rating: str | None = None
    level: str | None = None
    advisories: list[Any] | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | None = None
    guid: str | None = None
    original: bool | None = None
    variant: str | None = None
    season_guid: str | None = None
    media_guid: str | None = None
    is_premium_only: bool | None = None
    roles: list[str] | None = None

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | None = None
    text_notation: str | None = None
    text_locale: str | None = None
    text_notation_reason: str | None = None
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    audio_notation_reason: str | None = None

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_id: str | None = None
    series_title: str | None = None
    series_slug_title: str | None = None
    season_id: str | None = None
    season_title: str | None = None
    season_slug_title: str | None = None
    season_number: int | None = None
    episode_number: int | None = None
    episode: str | None = None
    sequence_number: int | None = None
    season_display_number: str | None = None
    season_sequence_number: int | None = None
    duration_ms: int | None = None
    ad_breaks: list[AdBreak] | None = None
    episode_air_date: AwareDatetime | None = None
    upload_date: AwareDatetime | None = None
    availability_starts: AwareDatetime | None = None
    availability_ends: AwareDatetime | None = None
    eligible_region: str | None = None
    is_premium_only: bool | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    maturity_ratings: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    available_date: Any | None = None
    free_available_date: AwareDatetime | None = None
    premium_date: Any | None = None
    premium_available_date: AwareDatetime | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_clip: bool | None = None
    available_offline: bool | None = None
    linked_guid: str | None = None
    tenant_categories: list[str] | None = None
    subtitle_locales: list[str] | None = None
    availability_notes: str | None = None
    audio_locale: str | None = None
    versions: list[Version] | None = None
    closed_captions_available: bool | None = None
    identifier: str | None = None
    availability_status: str | None = None
    roles: list[str] | None = None
    language_presentation: LanguagePresentation | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    score: float | None = None
    rank: int | None = None
    popularity_score: int | None = None

class Up(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None

class Down(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    up: Up | None = None
    down: Down | None = None
    total: int | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    external_id: str | None = None
    channel_id: str | None = None
    linked_resource_key: str | None = None
    new: bool | None = None
    title: str | None = None
    description: str | None = None
    promo_title: str | None = None
    promo_description: str | None = None
    type: str | None = None
    slug: str | None = None
    slug_title: str | None = None
    images: Images | None = None
    localized_images: LocalizedImages | None = None
    episode_metadata: EpisodeMetadata | None = None
    search_metadata: SearchMetadata | None = None
    language_presentation: LanguagePresentation | None = None
    rating: Rating | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    items: list[Item] | None = None
    count: int | None = None

class SearchEpisodeModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | None = None
    total: int | None = None
    meta: dict[str, Any] | None = None
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

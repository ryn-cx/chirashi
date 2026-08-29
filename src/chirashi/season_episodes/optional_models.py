from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict
from typing import Any

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | None = None
    rating: str | None = None
    level: str | None = None

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

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

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

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | None = None
    text_notation: str | None = None
    text_locale: str | None = None
    text_notation_reason: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    channel_id: str | None = None
    series_id: str | None = None
    series_title: str | None = None
    series_slug_title: str | None = None
    season_id: str | None = None
    season_title: str | None = None
    season_slug_title: str | None = None
    season_number: int | None = None
    episode: str | None = None
    episode_number: int | None = None
    sequence_number: int | None = None
    season_display_number: str | None = None
    season_sequence_number: int | None = None
    production_episode_id: str | None = None
    title: str | None = None
    slug_title: str | None = None
    description: str | None = None
    next_episode_id: str | None = None
    next_episode_title: str | None = None
    hd_flag: bool | None = None
    maturity_ratings: list[str] | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    episode_air_date: AwareDatetime | None = None
    upload_date: AwareDatetime | None = None
    availability_starts: AwareDatetime | None = None
    availability_ends: AwareDatetime | None = None
    eligible_region: str | None = None
    available_date: Any | None = None
    free_available_date: AwareDatetime | None = None
    premium_date: Any | None = None
    premium_available_date: AwareDatetime | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_clip: bool | None = None
    seo_title: str | None = None
    seo_description: str | None = None
    season_tags: list[Any] | None = None
    available_offline: bool | None = None
    subtitle_locales: list[str] | None = None
    availability_notes: str | None = None
    audio_locale: str | None = None
    versions: list[Version] | None = None
    closed_captions_available: bool | None = None
    identifier: str | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    media_type: str | None = None
    slug: str | None = None
    images: Images | None = None
    localized_images: LocalizedImages | None = None
    duration_ms: int | None = None
    ad_breaks: list[AdBreak] | None = None
    is_premium_only: bool | None = None
    listing_id: str | None = None
    recent_audio_locale: str | None = None
    recent_variant: str | None = None
    availability_status: str | None = None
    language_presentation: LanguagePresentation | None = None
    roles: list[str] | None = None

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    versions_considered: bool | None = None

class SeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | None = None
    total: int | None = None
    meta: Meta | None = None
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

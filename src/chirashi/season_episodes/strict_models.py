from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    system: str
    rating: str
    level: str

class Version(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_locale: str
    guid: str
    original: bool
    variant: str
    season_guid: str
    media_guid: str
    is_premium_only: bool
    roles: list[str]

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: list[list[ThumbnailItem]]

class LocalizedImages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: str

class AdBreak(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    offset_ms: int

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    text_locale: str | None = None
    text_notation_reason: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    channel_id: str
    series_id: str
    series_title: str
    series_slug_title: str
    season_id: str
    season_title: str
    season_slug_title: str
    season_number: int
    episode: str
    episode_number: int | None
    sequence_number: int | float
    season_display_number: str
    season_sequence_number: int
    production_episode_id: str
    title: str
    slug_title: str
    description: str
    next_episode_id: str
    next_episode_title: str | None = None
    hd_flag: bool
    maturity_ratings: list[str]
    extended_maturity_rating: ExtendedMaturityRating
    is_mature: bool
    mature_blocked: bool
    episode_air_date: AwareDatetime
    upload_date: AwareDatetime
    availability_starts: AwareDatetime
    availability_ends: AwareDatetime
    eligible_region: str
    available_date: None
    free_available_date: AwareDatetime
    premium_date: None
    premium_available_date: AwareDatetime
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    seo_title: str
    seo_description: str
    season_tags: list[str]
    available_offline: bool
    subtitle_locales: list[str]
    availability_notes: str
    audio_locale: str
    versions: list[Version]
    closed_captions_available: bool
    identifier: str
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem]
    media_type: str
    slug: str
    images: Images
    localized_images: LocalizedImages
    duration_ms: int
    ad_breaks: list[AdBreak]
    is_premium_only: bool
    listing_id: str
    recent_audio_locale: str
    recent_variant: str
    availability_status: str
    language_presentation: LanguagePresentation
    roles: list[str]

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    versions_considered: bool | None = None

class SeasonEpisodesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]
    total: int
    meta: Meta
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

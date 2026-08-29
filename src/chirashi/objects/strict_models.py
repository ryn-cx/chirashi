from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel
from typing import Any

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

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    system: str
    rating: str
    level: str

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

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

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    series_id: str
    series_title: str
    series_slug_title: str
    season_id: str
    season_title: str
    season_slug_title: str
    season_number: int
    season_display_number: str
    season_sequence_number: int
    episode: str
    episode_number: int
    sequence_number: int
    duration_ms: int
    ad_breaks: list[AdBreak]
    episode_air_date: AwareDatetime
    upload_date: AwareDatetime
    availability_starts: AwareDatetime
    availability_ends: AwareDatetime
    eligible_region: str
    is_premium_only: bool
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool
    mature_blocked: bool
    available_date: AwareDatetime
    free_available_date: AwareDatetime
    premium_date: None
    premium_available_date: AwareDatetime
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    available_offline: bool
    tenant_categories: list[str]
    subtitle_locales: list[str]
    availability_notes: str
    audio_locale: str
    versions: list[Version]
    closed_captions_available: bool
    identifier: str
    availability_status: str
    roles: list[str]

class Up(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str

class Down(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str

class Rating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    up: Up
    down: Down
    total: int

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    text_locale: str | None = None
    audio_notation_reason: str | None = None
    text_notation_reason: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    external_id: str
    channel_id: str
    title: str
    description: str
    type: str
    slug: str
    slug_title: str
    images: Images
    localized_images: LocalizedImages
    episode_metadata: EpisodeMetadata
    rating: Rating
    linked_resource_key: str
    language_presentation: LanguagePresentation

class ObjectsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]
    total: int
    meta: dict[str, Any]
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

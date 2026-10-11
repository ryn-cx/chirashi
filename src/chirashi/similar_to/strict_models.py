from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class Field1s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    percentage: int
    unit: str

class Field2s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    percentage: int
    unit: str

class Field3s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    percentage: int
    unit: str

class Field4s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    percentage: int
    unit: str

class Field5s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    percentage: int
    unit: str

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
    field_1s: Field1s | None = Field(None, alias='1s')
    field_2s: Field2s | None = Field(None, alias='2s')
    field_3s: Field3s | None = Field(None, alias='3s')
    field_4s: Field4s | None = Field(None, alias='4s')
    field_5s: Field5s | None = Field(None, alias='5s')
    average: str | None = None
    total: int
    up: Up | None = None
    down: Down | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    popularity_score: int | float
    rank: int
    score: float

class PosterTallItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class PosterWideItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class PromoImageItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_tall: list[list[PosterTallItem]] | None = None
    poster_wide: list[list[PosterWideItem]] | None = None
    promo_image: list[list[PromoImageItem]] | None = None
    thumbnail: list[list[ThumbnailItem]] | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    level: str | None = None
    rating: str | None = None
    system: str | None = None

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class Award(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_url: str
    is_current_award: bool
    is_winner: bool
    text: str

class Images1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]

class Livestream(BaseModel):
    model_config = ConfigDict(defer_build=True)
    countdown_visibility: int
    end_date: AwareDatetime
    episode_end_date: AwareDatetime
    episode_id: str
    episode_start_date: AwareDatetime
    images: Images1
    start_date: AwareDatetime

class SeriesMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_locales: list[str]
    availability_notes: str
    episode_count: int
    extended_description: str
    extended_maturity_rating: ExtendedMaturityRating
    is_dubbed: bool
    is_mature: bool
    is_simulcast: bool
    is_subbed: bool
    language_presentation: LanguagePresentation
    mature_blocked: bool
    maturity_ratings: list[str]
    season_count: int
    series_launch_year: int
    subtitle_locales: list[str]
    tenant_categories: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    awards: list[Award] | None = None
    livestream: Livestream | None = None

class AdBreak(BaseModel):
    model_config = ConfigDict(defer_build=True)
    offset_ms: int
    type: str

class ExtendedMaturityRating1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    level: str
    rating: str
    system: str

class Version(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_locale: str
    guid: str
    is_premium_only: bool
    media_guid: str
    original: bool
    roles: list[str]
    season_guid: str
    variant: str

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ad_breaks: list[AdBreak]
    audio_locale: str
    availability_ends: AwareDatetime
    availability_notes: str
    availability_starts: AwareDatetime
    availability_status: str
    available_date: None
    available_offline: bool
    closed_captions_available: bool
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    duration_ms: int
    eligible_region: str
    episode: str
    episode_air_date: AwareDatetime
    episode_number: int
    extended_maturity_rating: ExtendedMaturityRating1
    free_available_date: AwareDatetime
    identifier: str
    is_clip: bool
    is_dubbed: bool
    is_mature: bool
    is_premium_only: bool
    is_subbed: bool
    language_presentation: LanguagePresentation
    mature_blocked: bool
    maturity_ratings: list[str]
    premium_available_date: AwareDatetime
    premium_date: None
    roles: list[str]
    season_display_number: str
    season_id: str
    season_number: int
    season_sequence_number: int
    season_slug_title: str
    season_title: str
    sequence_number: int
    series_id: str
    series_slug_title: str
    series_title: str
    subtitle_locales: list[str]
    upload_date: AwareDatetime
    versions: list[Version]

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    new: bool
    slug: str
    rating: Rating
    search_metadata: SearchMetadata
    slug_title: str
    channel_id: str
    images: Images
    series_metadata: SeriesMetadata | None = None
    title: str
    promo_title: str
    description: str
    linked_resource_key: str
    id: str
    promo_description: str
    external_id: str
    episode_metadata: EpisodeMetadata | None = None

class SimilarToModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total: int
    data: list[Datum]
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

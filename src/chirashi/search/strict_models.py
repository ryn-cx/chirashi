from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID

class PosterWideItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class PosterTallItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class PromoImageItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Thumbnail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_wide: list[list[PosterWideItem]] | None = None
    poster_tall: list[list[PosterTallItem]] | None = None
    promo_image: list[list[PromoImageItem]] | None = None
    thumbnail: list[list[ThumbnailItem] | Thumbnail] | None = None

class LocalizedImages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_wide: str | None = None
    poster_tall: str | None = None
    thumbnail: str | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    system: str
    rating: str
    level: str
    advisories: list[None]

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    text_locale: str | None = None
    audio_notation_reason: str | None = None
    text_notation_reason: str | None = None

class Award(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool

class SeriesMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability_status: str
    extended_description: str
    episode_count: int
    season_count: int
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    linked_guid: str
    availability_notes: str
    audio_locales: list[str]
    subtitle_locales: list[str]
    series_launch_year: int
    tenant_categories: list[str]
    language_presentation: LanguagePresentation
    awards: list[Award] | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    score: float
    rank: int | None = None
    popularity_score: int | float | None = None

class Field1s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str
    percentage: int

class Field2s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str
    percentage: int

class Field3s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str
    percentage: int

class Field4s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str
    percentage: int

class Field5s(BaseModel):
    model_config = ConfigDict(defer_build=True)
    displayed: str
    unit: str
    percentage: int

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

class AdBreak(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    offset_ms: int

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

class LanguagePresentation2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    is_original_audio: bool | None = None
    text_locale: str | None = None
    text_notation_reason: str | None = None
    audio_locale: str | None = None
    audio_notation_reason: str | None = None

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    series_id: str
    series_title: str
    series_slug_title: str
    season_id: str
    season_title: str
    season_slug_title: str
    season_number: int
    episode_number: int
    episode: str
    sequence_number: int
    season_display_number: str
    season_sequence_number: int
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
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem]
    is_mature: bool
    mature_blocked: bool
    available_date: None
    free_available_date: AwareDatetime
    premium_date: None
    premium_available_date: AwareDatetime
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    available_offline: bool
    linked_guid: str
    tenant_categories: list[str]
    subtitle_locales: list[str]
    availability_notes: str
    audio_locale: str
    versions: list[Version]
    closed_captions_available: bool
    identifier: str
    availability_status: str
    roles: list[str]
    language_presentation: LanguagePresentation2

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Artist(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    name: str
    slug: str

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_value: str = Field(..., alias='displayValue')
    id: str

class MainArtistItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class Artists(BaseModel):
    model_config = ConfigDict(defer_build=True)
    main_artist: list[MainArtistItem] = Field(..., alias='MainArtist')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    external_id: str | None = None
    channel_id: str | None = None
    linked_resource_key: str | None = None
    new: bool
    title: str
    description: str
    promo_title: str | None = None
    promo_description: str | None = None
    type: str
    slug: str
    slug_title: str | None = None
    last_public: AwareDatetime | None = None
    images: Images
    localized_images: LocalizedImages | None = None
    series_metadata: SeriesMetadata | None = None
    search_metadata: SearchMetadata
    language_presentation: LanguagePresentation | None = None
    rating: Rating | None = None
    episode_metadata: EpisodeMetadata | None = None
    streams_link: str | None = None
    availability: Availability | None = None
    copyright: str | None = None
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    artist: Artist | None = None
    genres: list[Genre] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    is_public: bool | None = Field(None, alias='isPublic')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    hash: UUID | None = None
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    duration_ms: int | None = Field(None, alias='durationMs')
    licensor: str | None = None
    artists: Artists | None = None
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    is_mature: bool | None = Field(None, alias='isMature')
    anime_ids: list[str] | None = Field(None, alias='animeIds')

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    items: list[Item]
    count: int

class SearchModel(BaseModel):
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

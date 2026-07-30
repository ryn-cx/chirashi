from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from typing import Any
from uuid import UUID

class PosterWideItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class PosterTallItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class PromoImageItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class Thumbnail(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    poster_wide: list[list[PosterWideItem]] | None = None
    poster_tall: list[list[PosterTallItem]] | None = None
    promo_image: list[list[PromoImageItem]] | None = None
    thumbnail: list[list[ThumbnailItem] | Thumbnail] | None = None

class ExtendedMaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    system: str
    rating: str
    level: str
    advisories: list[None]

class ContentDescriptorsWithSymbolItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class LanguagePresentation(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_notation: str
    text_notation: str

class Award(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool

class SeriesMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class SearchMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    score: float
    rank: int | None = None
    popularity_score: int | float | None = None

class Field1s(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str
    percentage: int

class Field2s(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str
    percentage: int

class Field3s(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str
    percentage: int

class Field4s(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str
    percentage: int

class Field5s(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str
    percentage: int

class Up(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str

class Down(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_1s: Field1s | None = Field(None, alias='1s')
    field_2s: Field2s | None = Field(None, alias='2s')
    field_3s: Field3s | None = Field(None, alias='3s')
    field_4s: Field4s | None = Field(None, alias='4s')
    field_5s: Field5s | None = Field(None, alias='5s')
    average: str | None = None
    total: int
    up: Up | None = None
    down: Down | None = None

class AdBreak(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    offset_ms: int

class Version(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_locale: str
    guid: str
    original: bool
    variant: str
    season_guid: str
    media_guid: str
    is_premium_only: bool
    roles: list[str]

class EpisodeMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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
    language_presentation: LanguagePresentation

class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    slug: str

class MainArtistItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class Artists(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    main_artist: list[MainArtistItem] = Field(..., alias='MainArtist')

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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
    series_metadata: SeriesMetadata | None = None
    search_metadata: SearchMetadata
    language_presentation: LanguagePresentation | None = None
    rating: Rating | None = None
    episode_metadata: EpisodeMetadata | None = None
    hash: UUID | None = None
    artist: Artist | None = None
    is_mature: bool | None = Field(None, alias='isMature')
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    streams_link: str | None = None
    artists: Artists | None = None
    availability: Availability | None = None
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    is_public: bool | None = Field(None, alias='isPublic')
    duration_ms: int | None = Field(None, alias='durationMs')
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    genres: list[Genre] | None = None
    licensor: str | None = None
    copyright: str | None = None
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    anime_ids: list[str] | None = Field(None, alias='animeIds')

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    items: list[Item]
    count: int

class SearchModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]
    total: int
    meta: dict[str, Any]

# ruff: noqa: D100, D101
from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Availability(BaseModel):
    model_config = ConfigDict(extra="forbid")
    end_date: AwareDatetime = Field(..., alias="endDate")
    start_date: AwareDatetime = Field(..., alias="startDate")


class Artist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    slug: str


class Genre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display_value: str = Field(..., alias="displayValue")
    id: str


class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    score: float


class Thumbnail(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[Thumbnail | list[ThumbnailItem]] | None = None
    poster_tall: list[list[PosterTallItem]] | None = None
    poster_wide: list[list[PosterWideItem]] | None = None


class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias="sequenceNumber")
    slug: str


class FeaturedArtistItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias="sequenceNumber")
    slug: str


class Artists(BaseModel):
    model_config = ConfigDict(extra="forbid")
    main_artist: list[MainArtistItem] = Field(..., alias="MainArtist")
    featured_artist: list[FeaturedArtistItem] | None = Field(
        None,
        alias="FeaturedArtist",
    )


class Award(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon_url: str
    is_current_award: bool
    is_winner: bool
    text: str


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str
    rating: str
    system: str


class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locales: list[str]
    availability_notes: str
    awards: list[Award] | None = None
    content_descriptors: list[str] | None = None
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
    tenant_categories: list[str]


class Field1s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field2s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field3s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field4s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field5s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Up(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str


class Down(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str


class Rating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    field_1s: Field1s | None = Field(None, alias="1s")
    field_2s: Field2s | None = Field(None, alias="2s")
    field_3s: Field3s | None = Field(None, alias="3s")
    field_4s: Field4s | None = Field(None, alias="4s")
    field_5s: Field5s | None = Field(None, alias="5s")
    average: str | None = None
    up: Up | None = None
    down: Down | None = None


class AdBreak(BaseModel):
    model_config = ConfigDict(extra="forbid")
    offset_ms: int
    type: str


class Version(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locale: str
    guid: str
    is_premium_only: bool
    media_guid: str
    original: bool
    roles: list[str]
    season_guid: str
    variant: str


class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ad_breaks: list[AdBreak]
    audio_locale: str
    availability_ends: AwareDatetime
    availability_notes: str
    availability_starts: AwareDatetime
    availability_status: str
    available_date: None
    available_offline: bool
    closed_captions_available: bool
    content_descriptors: list[str]
    duration_ms: int
    eligible_region: str
    episode: str
    episode_air_date: AwareDatetime
    episode_number: int | None
    extended_maturity_rating: ExtendedMaturityRating
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
    tenant_categories: list[str] | None = None
    upload_date: AwareDatetime
    versions: list[Version]


class MovieListingMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ad_breaks: list[AdBreak]
    availability_notes: str
    availability_status: str
    available_date: None
    available_offline: bool
    content_descriptors: list[str]
    duration_ms: int
    extended_description: str
    extended_maturity_rating: ExtendedMaturityRating
    first_movie_id: str
    free_available_date: AwareDatetime
    is_dubbed: bool
    is_mature: bool
    is_premium_only: bool
    is_subbed: bool
    mature_blocked: bool
    maturity_ratings: list[str]
    movie_release_year: int
    premium_available_date: AwareDatetime
    premium_date: None
    subtitle_locales: list[None]
    tenant_categories: list[str]


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    is_public: bool | None = Field(None, alias="isPublic")
    title: str
    streams_link: str | None = None
    copyright: str | None = None
    availability: Availability | None = None
    original_release: AwareDatetime | None = Field(None, alias="originalRelease")
    duration_ms: int | None = Field(None, alias="durationMs")
    mature_blocked: bool | None = Field(None, alias="matureBlocked")
    sequence_number: int | None = Field(None, alias="sequenceNumber")
    publish_date: AwareDatetime | None = Field(None, alias="publishDate")
    artist: Artist | None = None
    is_mature: bool | None = Field(None, alias="isMature")
    slug: str
    created_at: str | None = Field(None, alias="createdAt")
    is_premium_only: bool | None = Field(None, alias="isPremiumOnly")
    new: bool
    display_artist_name_required: bool | None = Field(
        None,
        alias="displayArtistNameRequired",
    )
    id: str
    hash: str | None = None
    genres: list[Genre] | None = None
    display_artist_name: str | None = Field(None, alias="displayArtistName")
    type: str
    search_metadata: SearchMetadata
    description: str
    images: Images
    licensor: str | None = None
    maturity_ratings: dict[str, Any] | None = Field(None, alias="maturityRatings")
    ready_to_publish: bool | None = Field(None, alias="readyToPublish")
    anime_ids: list[str] | None = Field(None, alias="animeIds")
    artists: Artists | None = None
    updated_at: str | None = Field(None, alias="updatedAt")
    promo_title: str | None = None
    series_metadata: SeriesMetadata | None = None
    promo_description: str | None = None
    external_id: str | None = None
    linked_resource_key: str | None = None
    channel_id: str | None = None
    rating: Rating | None = None
    slug_title: str | None = None
    episode_metadata: EpisodeMetadata | None = None
    movie_listing_metadata: MovieListingMetadata | None = None


class Datum(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    count: int
    items: list[Item]


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    q: str
    n: int
    type: str
    ratings: str
    preferred_audio_language: str
    locale: str


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    referer: str


class Chirashi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    params: Params
    headers: Headers
    url: str
    timestamp: AwareDatetime


class Search(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    data: list[Datum]
    meta: dict[str, Any]
    chirashi: Chirashi

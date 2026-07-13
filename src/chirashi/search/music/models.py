# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class Images(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[ThumbnailItem]


class SearchMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    score: float


class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display_value: str = Field(..., alias="displayValue")
    id: str


class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    slug: str


class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    end_date: AwareDatetime = Field(..., alias="endDate")
    start_date: AwareDatetime = Field(..., alias="startDate")


class MainArtistItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias="sequenceNumber")
    slug: str


class FeaturedArtistItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias="sequenceNumber")
    slug: str


class Artists(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    main_artist: list[MainArtistItem] = Field(..., alias="MainArtist")
    featured_artist: list[FeaturedArtistItem] | None = Field(
        None,
        alias="FeaturedArtist",
    )


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    type: str
    title: str
    description: str
    slug: str
    images: Images
    search_metadata: SearchMetadata
    is_mature: bool = Field(..., alias="isMature")
    display_artist_name_required: bool = Field(..., alias="displayArtistNameRequired")
    licensor: str
    updated_at: str = Field(..., alias="updatedAt")
    new: bool
    mature_blocked: bool = Field(..., alias="matureBlocked")
    is_public: bool = Field(..., alias="isPublic")
    sequence_number: int = Field(..., alias="sequenceNumber")
    created_at: str = Field(..., alias="createdAt")
    is_premium_only: bool = Field(..., alias="isPremiumOnly")
    ready_to_publish: bool = Field(..., alias="readyToPublish")
    copyright: str
    genres: list[Genre]
    artist: Artist
    display_artist_name: str = Field(..., alias="displayArtistName")
    availability: Availability
    duration_ms: int = Field(..., alias="durationMs")
    original_release: AwareDatetime = Field(..., alias="originalRelease")
    hash: str
    anime_ids: list[str] | None = Field(None, alias="animeIds")
    artists: Artists
    streams_link: str
    maturity_ratings: dict[str, Any] = Field(..., alias="maturityRatings")
    publish_date: AwareDatetime = Field(..., alias="publishDate")


class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    items: list[Item]
    count: int


class SearchMusicModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: list[Datum]
    total: int
    meta: dict[str, Any]

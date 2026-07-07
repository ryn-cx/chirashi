# ruff: noqa: D100, D101
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field, RootModel


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


class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display_value: str = Field(..., alias="displayValue")
    id: str


class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    end_date: AwareDatetime = Field(..., alias="endDate")
    start_date: AwareDatetime = Field(..., alias="startDate")


class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    slug: str


class SearchMusicItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    new: bool
    title: str
    description: str
    type: str
    slug: str
    images: Images
    search_metadata: SearchMetadata
    artists: Artists
    maturity_ratings: dict[str, Any] = Field(..., alias="maturityRatings")
    genres: list[Genre]
    is_mature: bool = Field(..., alias="isMature")
    is_public: bool = Field(..., alias="isPublic")
    licensor: str
    duration_ms: int = Field(..., alias="durationMs")
    availability: Availability
    created_at: str = Field(..., alias="createdAt")
    ready_to_publish: bool = Field(..., alias="readyToPublish")
    anime_ids: list[str] = Field(..., alias="animeIds")
    hash: str
    sequence_number: int = Field(..., alias="sequenceNumber")
    is_premium_only: bool = Field(..., alias="isPremiumOnly")
    publish_date: AwareDatetime = Field(..., alias="publishDate")
    updated_at: str = Field(..., alias="updatedAt")
    artist: Artist
    display_artist_name_required: bool = Field(..., alias="displayArtistNameRequired")
    streams_link: str
    display_artist_name: str = Field(..., alias="displayArtistName")
    original_release: AwareDatetime = Field(..., alias="originalRelease")
    mature_blocked: bool = Field(..., alias="matureBlocked")
    copyright: str


class SearchMusic(RootModel[list[SearchMusicItem]]):
    root: list[SearchMusicItem]

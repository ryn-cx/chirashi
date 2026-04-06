# ruff: noqa: D100, D101
from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel


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


class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[ThumbnailItem]


class MainArtistItem(BaseModel):
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


class SearchMusicItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    is_public: bool = Field(..., alias="isPublic")
    title: str
    streams_link: str
    copyright: str
    availability: Availability
    original_release: AwareDatetime = Field(..., alias="originalRelease")
    duration_ms: int = Field(..., alias="durationMs")
    mature_blocked: bool = Field(..., alias="matureBlocked")
    sequence_number: int = Field(..., alias="sequenceNumber")
    publish_date: AwareDatetime = Field(..., alias="publishDate")
    artist: Artist
    is_mature: bool = Field(..., alias="isMature")
    slug: str
    created_at: str = Field(..., alias="createdAt")
    is_premium_only: bool = Field(..., alias="isPremiumOnly")
    new: bool
    display_artist_name_required: bool = Field(..., alias="displayArtistNameRequired")
    id: str
    hash: str
    genres: list[Genre]
    display_artist_name: str = Field(..., alias="displayArtistName")
    type: str
    search_metadata: SearchMetadata
    description: str
    images: Images
    licensor: str
    maturity_ratings: dict[str, Any] = Field(..., alias="maturityRatings")
    ready_to_publish: bool = Field(..., alias="readyToPublish")
    anime_ids: list[str] = Field(..., alias="animeIds")
    artists: Artists
    updated_at: str = Field(..., alias="updatedAt")


class SearchMusic(RootModel[list[SearchMusicItem]]):
    root: list[SearchMusicItem]

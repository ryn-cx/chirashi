from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    height: int
    source: str
    type: str
    width: int

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    thumbnail: list[ThumbnailItem]

class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    slug: str

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class MainArtistItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class FeaturedArtistItem(GAPIBaseModel):
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
    featured_artist: list[FeaturedArtistItem] | None = Field(None, alias='FeaturedArtist')

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_mature: bool = Field(..., alias='isMature')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    images: Images
    is_public: bool = Field(..., alias='isPublic')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    artist: Artist
    availability: Availability
    id: str
    mature_blocked: bool = Field(..., alias='matureBlocked')
    sequence_number: int = Field(..., alias='sequenceNumber')
    type: str
    genres: list[Genre]
    hash: UUID
    artists: Artists
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    title: str
    anime_ids: list[str] = Field(..., alias='animeIds')
    copyright: str
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name: str = Field(..., alias='displayArtistName')
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    licensor: str
    streams_link: str
    description: str
    duration_ms: int = Field(..., alias='durationMs')
    slug: str

class ArtistMusicVideosModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]

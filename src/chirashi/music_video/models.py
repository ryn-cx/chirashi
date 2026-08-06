from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from uuid import UUID
from typing import Any

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    slug: str

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    height: int
    source: str
    type: str
    width: int

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    thumbnail: list[ThumbnailItem]

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

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_artist_name: str = Field(..., alias='displayArtistName')
    hash: UUID
    mature_blocked: bool = Field(..., alias='matureBlocked')
    duration_ms: int = Field(..., alias='durationMs')
    is_public: bool = Field(..., alias='isPublic')
    anime_ids: list[str] = Field(..., alias='animeIds')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    is_mature: bool = Field(..., alias='isMature')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    streams_link: str
    availability: Availability
    licensor: str
    title: str
    artist: Artist
    copyright: str
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    genres: list[Genre]
    id: str
    images: Images
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str
    type: str
    artists: Artists
    created_at: AwareDatetime = Field(..., alias='createdAt')
    description: str

class MusicVideoModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]

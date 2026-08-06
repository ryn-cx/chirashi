from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from uuid import UUID
from typing import Any

class Artist(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    slug: str

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

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

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    artist: Artist
    availability: Availability
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    images: Images
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    sequence_number: int = Field(..., alias='sequenceNumber')
    display_artist_name: str = Field(..., alias='displayArtistName')
    hash: UUID
    is_mature: bool = Field(..., alias='isMature')
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    title: str
    type: str
    artists: Artists
    copyright: str
    id: str
    licensor: str
    mature_blocked: bool = Field(..., alias='matureBlocked')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    description: str
    duration_ms: int = Field(..., alias='durationMs')
    genres: list[Genre]
    is_public: bool = Field(..., alias='isPublic')
    slug: str
    streams_link: str

class ConcertModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]

from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from uuid import UUID
from typing import Any

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

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    slug: str
    streams_link: str
    artists: Artists
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    is_public: bool = Field(..., alias='isPublic')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    title: str
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    availability: Availability
    description: str
    duration_ms: int = Field(..., alias='durationMs')
    id: str
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    licensor: str
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    sequence_number: int = Field(..., alias='sequenceNumber')
    copyright: str
    display_artist_name: str = Field(..., alias='displayArtistName')
    hash: UUID
    images: Images
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    type: str
    artist: Artist
    genres: list[Genre]
    is_mature: bool = Field(..., alias='isMature')
    mature_blocked: bool = Field(..., alias='matureBlocked')

class ArtistConcertsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]

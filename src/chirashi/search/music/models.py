from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from uuid import UUID
from typing import Any

class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    thumbnail: list[ThumbnailItem]

class SearchMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    score: float

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

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str
    title: str
    description: str
    slug: str
    images: Images
    search_metadata: SearchMetadata
    is_public: bool = Field(..., alias='isPublic')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    new: bool
    copyright: str
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    artist: Artist
    artists: Artists
    sequence_number: int = Field(..., alias='sequenceNumber')
    is_mature: bool = Field(..., alias='isMature')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    duration_ms: int = Field(..., alias='durationMs')
    genres: list[Genre]
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    anime_ids: list[str] = Field(..., alias='animeIds')
    licensor: str
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    mature_blocked: bool = Field(..., alias='matureBlocked')
    availability: Availability
    streams_link: str
    hash: UUID
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name: str = Field(..., alias='displayArtistName')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    items: list[Item]
    count: int

class SearchMusicModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]
    total: int
    meta: dict[str, Any]

from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    thumbnail: list[ThumbnailItem]

class Genre(BaseModel):
    display_value: str = Field(..., alias='displayValue')
    id: str

class Artist(BaseModel):
    id: str
    name: str
    slug: str

class Availability(BaseModel):
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class MainArtistItem(BaseModel):
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class FeaturedArtistItem(BaseModel):
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class Artists(BaseModel):
    main_artist: list[MainArtistItem] = Field(..., alias='MainArtist')
    featured_artist: list[FeaturedArtistItem] | None = Field(None, alias='FeaturedArtist')

class Datum(BaseModel):
    images: Images
    sequence_number: int = Field(..., alias='sequenceNumber')
    copyright: str
    display_artist_name: str = Field(..., alias='displayArtistName')
    genres: list[Genre]
    licensor: str
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    description: str
    id: str
    is_mature: bool = Field(..., alias='isMature')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    artist: Artist
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    mature_blocked: bool = Field(..., alias='matureBlocked')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    anime_ids: list[str] = Field(..., alias='animeIds')
    availability: Availability
    duration_ms: int = Field(..., alias='durationMs')
    is_public: bool = Field(..., alias='isPublic')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    title: str
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    hash: UUID
    artists: Artists
    slug: str
    type: str
    streams_link: str

class ArtistMusicVideosModel(BaseModel):
    total: int
    data: list[Datum]
    meta: dict[str, Any]
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input

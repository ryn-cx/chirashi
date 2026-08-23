from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

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

class Artists(BaseModel):
    main_artist: list[MainArtistItem] = Field(..., alias='MainArtist')

class Genre(BaseModel):
    display_value: str = Field(..., alias='displayValue')
    id: str

class ThumbnailItem(BaseModel):
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    thumbnail: list[ThumbnailItem]

class Datum(BaseModel):
    id: str
    artist: Artist
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    licensor: str
    is_mature: bool = Field(..., alias='isMature')
    sequence_number: int = Field(..., alias='sequenceNumber')
    streams_link: str
    created_at: AwareDatetime = Field(..., alias='createdAt')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    type: str
    title: str
    hash: UUID
    anime_ids: list[str] = Field(..., alias='animeIds')
    availability: Availability
    display_artist_name: str = Field(..., alias='displayArtistName')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    artists: Artists
    copyright: str
    genres: list[Genre]
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    images: Images
    description: str
    duration_ms: int = Field(..., alias='durationMs')
    is_public: bool = Field(..., alias='isPublic')
    mature_blocked: bool = Field(..., alias='matureBlocked')
    slug: str

class MusicVideoModel(BaseModel):
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

from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: list[ThumbnailItem]

class Artist(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    name: str
    slug: str

class MainArtistItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    connector: str
    id: str
    name: str
    roles: list[str]
    sequence_number: int = Field(..., alias='sequenceNumber')
    slug: str

class Artists(BaseModel):
    model_config = ConfigDict(defer_build=True)
    main_artist: list[MainArtistItem] = Field(..., alias='MainArtist')

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_value: str = Field(..., alias='displayValue')
    id: str

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability
    copyright: str
    created_at: AwareDatetime = Field(..., alias='createdAt')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    duration_ms: int = Field(..., alias='durationMs')
    images: Images
    slug: str
    description: str
    hash: UUID
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    is_public: bool = Field(..., alias='isPublic')
    licensor: str
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    type: str
    artist: Artist
    artists: Artists
    is_mature: bool = Field(..., alias='isMature')
    mature_blocked: bool = Field(..., alias='matureBlocked')
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    streams_link: str
    display_artist_name: str = Field(..., alias='displayArtistName')
    genres: list[Genre]
    id: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title: str
    updated_at: AwareDatetime = Field(..., alias='updatedAt')

class ConcertModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

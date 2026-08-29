from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: list[ThumbnailItem]

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

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_value: str = Field(..., alias='displayValue')
    id: str

class Artist(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    name: str
    slug: str

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    created_at: AwareDatetime = Field(..., alias='createdAt')
    id: str
    is_mature: bool = Field(..., alias='isMature')
    licensor: str
    mature_blocked: bool = Field(..., alias='matureBlocked')
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    images: Images
    is_public: bool = Field(..., alias='isPublic')
    title: str
    streams_link: str
    artists: Artists
    availability: Availability
    copyright: str
    description: str
    duration_ms: int = Field(..., alias='durationMs')
    genres: list[Genre]
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    sequence_number: int = Field(..., alias='sequenceNumber')
    artist: Artist
    display_artist_name: str = Field(..., alias='displayArtistName')
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')
    hash: UUID
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    slug: str
    type: str

class ArtistConcertsModel(BaseModel):
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

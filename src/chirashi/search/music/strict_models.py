from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    thumbnail: list[ThumbnailItem]

class SearchMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    score: float

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_value: str = Field(..., alias='displayValue')
    id: str

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

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    end_date: AwareDatetime = Field(..., alias='endDate')
    start_date: AwareDatetime = Field(..., alias='startDate')

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    type: str
    title: str
    description: str
    slug: str
    images: Images
    search_metadata: SearchMetadata
    genres: list[Genre]
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    artist: Artist
    maturity_ratings: dict[str, Any] = Field(..., alias='maturityRatings')
    licensor: str
    new: bool
    mature_blocked: bool = Field(..., alias='matureBlocked')
    is_premium_only: bool = Field(..., alias='isPremiumOnly')
    is_public: bool = Field(..., alias='isPublic')
    anime_ids: list[str] = Field(..., alias='animeIds')
    artists: Artists
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    sequence_number: int = Field(..., alias='sequenceNumber')
    display_artist_name: str = Field(..., alias='displayArtistName')
    hash: UUID
    original_release: AwareDatetime = Field(..., alias='originalRelease')
    duration_ms: int = Field(..., alias='durationMs')
    is_mature: bool = Field(..., alias='isMature')
    availability: Availability
    copyright: str
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    created_at: AwareDatetime = Field(..., alias='createdAt')
    streams_link: str
    display_artist_name_required: bool = Field(..., alias='displayArtistNameRequired')

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    items: list[Item]
    count: int

class SearchMusicModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]
    total: int
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

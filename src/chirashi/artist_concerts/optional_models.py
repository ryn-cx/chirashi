from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail: list[ThumbnailItem] | None = None

class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    connector: str | None = None
    id: str | None = None
    name: str | None = None
    roles: list[str] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    slug: str | None = None

class Artists(BaseModel):
    model_config = ConfigDict(extra='ignore')
    main_artist: list[MainArtistItem] | None = Field(None, alias='MainArtist')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore')
    end_date: AwareDatetime | None = Field(None, alias='endDate')
    start_date: AwareDatetime | None = Field(None, alias='startDate')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    name: str | None = None
    slug: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    id: str | None = None
    is_mature: bool | None = Field(None, alias='isMature')
    licensor: str | None = None
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    images: Images | None = None
    is_public: bool | None = Field(None, alias='isPublic')
    title: str | None = None
    streams_link: str | None = None
    artists: Artists | None = None
    availability: Availability | None = None
    copyright: str | None = None
    description: str | None = None
    duration_ms: int | None = Field(None, alias='durationMs')
    genres: list[Genre] | None = None
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    artist: Artist | None = None
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    hash: UUID | None = None
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    slug: str | None = None
    type: str | None = None

class ArtistConcertsModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    total: int | None = None
    data: list[Datum] | None = None
    meta: dict[str, Any] | None = None
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

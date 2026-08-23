from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore')
    end_date: AwareDatetime | None = Field(None, alias='endDate')
    start_date: AwareDatetime | None = Field(None, alias='startDate')

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail: list[ThumbnailItem] | None = None

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    name: str | None = None
    slug: str | None = None

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

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    availability: Availability | None = None
    copyright: str | None = None
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    duration_ms: int | None = Field(None, alias='durationMs')
    images: Images | None = None
    slug: str | None = None
    description: str | None = None
    hash: UUID | None = None
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    is_public: bool | None = Field(None, alias='isPublic')
    licensor: str | None = None
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    type: str | None = None
    artist: Artist | None = None
    artists: Artists | None = None
    is_mature: bool | None = Field(None, alias='isMature')
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    streams_link: str | None = None
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    genres: list[Genre] | None = None
    id: str | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    title: str | None = None
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')

class ConcertModel(BaseModel):
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

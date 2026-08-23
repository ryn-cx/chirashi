from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    thumbnail: list[ThumbnailItem] | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    score: float | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

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

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore')
    end_date: AwareDatetime | None = Field(None, alias='endDate')
    start_date: AwareDatetime | None = Field(None, alias='startDate')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    type: str | None = None
    title: str | None = None
    description: str | None = None
    slug: str | None = None
    images: Images | None = None
    search_metadata: SearchMetadata | None = None
    genres: list[Genre] | None = None
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    artist: Artist | None = None
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    licensor: str | None = None
    new: bool | None = None
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    is_public: bool | None = Field(None, alias='isPublic')
    anime_ids: list[str] | None = Field(None, alias='animeIds')
    artists: Artists | None = None
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    hash: UUID | None = None
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    duration_ms: int | None = Field(None, alias='durationMs')
    is_mature: bool | None = Field(None, alias='isMature')
    availability: Availability | None = None
    copyright: str | None = None
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    streams_link: str | None = None
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    items: list[Item] | None = None
    count: int | None = None

class SearchMusicModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data: list[Datum] | None = None
    total: int | None = None
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

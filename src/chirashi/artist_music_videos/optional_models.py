from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: list[ThumbnailItem] | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    name: str | None = None
    slug: str | None = None

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_date: AwareDatetime | None = Field(None, alias='endDate')
    start_date: AwareDatetime | None = Field(None, alias='startDate')

class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | None = None
    id: str | None = None
    name: str | None = None
    roles: list[str] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    slug: str | None = None

class FeaturedArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | None = None
    id: str | None = None
    name: str | None = None
    roles: list[str] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    slug: str | None = None

class Artists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    main_artist: list[MainArtistItem] | None = Field(None, alias='MainArtist')
    featured_artist: list[FeaturedArtistItem] | None = Field(None, alias='FeaturedArtist')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    copyright: str | None = None
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    genres: list[Genre] | None = None
    licensor: str | None = None
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    description: str | None = None
    id: str | None = None
    is_mature: bool | None = Field(None, alias='isMature')
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    artist: Artist | None = None
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    anime_ids: list[str] | None = Field(None, alias='animeIds')
    availability: Availability | None = None
    duration_ms: int | None = Field(None, alias='durationMs')
    is_public: bool | None = Field(None, alias='isPublic')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    title: str | None = None
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    hash: UUID | None = None
    artists: Artists | None = None
    slug: str | None = None
    type: str | None = None
    streams_link: str | None = None

class ArtistMusicVideosModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
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

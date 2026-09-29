from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    thumbnail: list[ThumbnailItem] | Any = Field(default=None, union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | Any = Field(None, alias='displayValue', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_date: AwareDatetime | Any = Field(None, alias='endDate', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(None, alias='startDate', union_mode='left_to_right')

class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(None, alias='sequenceNumber', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class FeaturedArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(None, alias='sequenceNumber', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class Artists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    main_artist: list[MainArtistItem] | Any = Field(None, alias='MainArtist', union_mode='left_to_right')
    featured_artist: list[FeaturedArtistItem] | Any = Field(None, alias='FeaturedArtist', union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(None, alias='sequenceNumber', union_mode='left_to_right')
    copyright: str | Any = Field(default=None, union_mode='left_to_right')
    display_artist_name: str | Any = Field(None, alias='displayArtistName', union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    licensor: str | Any = Field(default=None, union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    is_mature: bool | Any = Field(None, alias='isMature', union_mode='left_to_right')
    maturity_ratings: dict[str, Any] | Any = Field(None, alias='maturityRatings', union_mode='left_to_right')
    artist: Artist | Any = Field(default=None, union_mode='left_to_right')
    created_at: AwareDatetime | Any = Field(None, alias='createdAt', union_mode='left_to_right')
    display_artist_name_required: bool | Any = Field(None, alias='displayArtistNameRequired', union_mode='left_to_right')
    mature_blocked: bool | Any = Field(None, alias='matureBlocked', union_mode='left_to_right')
    publish_date: AwareDatetime | Any = Field(None, alias='publishDate', union_mode='left_to_right')
    anime_ids: list[str] | Any = Field(None, alias='animeIds', union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    duration_ms: int | Any = Field(None, alias='durationMs', union_mode='left_to_right')
    is_public: bool | Any = Field(None, alias='isPublic', union_mode='left_to_right')
    original_release: AwareDatetime | Any = Field(None, alias='originalRelease', union_mode='left_to_right')
    ready_to_publish: bool | Any = Field(None, alias='readyToPublish', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(None, alias='isPremiumOnly', union_mode='left_to_right')
    hash: UUID | Any = Field(default=None, union_mode='left_to_right')
    artists: Artists | Any = Field(default=None, union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    streams_link: str | Any = Field(default=None, union_mode='left_to_right')

class ArtistMusicVideosModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total: int | Any = Field(default=None, union_mode='left_to_right')
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')
    meta: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
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

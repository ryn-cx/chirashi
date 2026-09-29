from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: list[PosterTallItem] | Any = Field(default=None, union_mode='left_to_right')
    poster_wide: list[PosterWideItem] | Any = Field(default=None, union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | Any = Field(None, alias='displayValue', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    is_public: bool | Any = Field(None, alias='isPublic', union_mode='left_to_right')
    ready_to_publish: bool | Any = Field(None, alias='readyToPublish', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    concerts: list[str] | Any = Field(default=None, union_mode='left_to_right')
    total_video_duration_ms: int | Any = Field(None, alias='totalVideoDurationMs', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    created_at: AwareDatetime | Any = Field(None, alias='createdAt', union_mode='left_to_right')
    publish_date: AwareDatetime | Any = Field(None, alias='publishDate', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    total_concert_duration_ms: int | Any = Field(None, alias='totalConcertDurationMs', union_mode='left_to_right')
    videos: list[str] | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class BrowseMusicModel(BaseModel):
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
